from urllib.parse import quote_plus

from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.utils import timezone
from django.db.models import Q

from taggit.models import Tag

# Create your views here.


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    # if not request.user.is_authenticated():
    #     raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        form.save_m2m()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    # if request.method == "POST":
    # 	print(request.POST)
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    if instance.draft or instance.publish > timezone.now().date():
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    share_string = quote_plus(instance.content)
    context = {
        "object": instance,
        "share_string": share_string,
    }
    return render(request, "post_detail.html", context)


def post_list(request, tag_slug=None):
    today = timezone.now().date()
    queryset_list = Post.objects.active()
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
        ).distinct()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        queryset_list = queryset_list.filter(tags__in=[tag])

    paginator = Paginator(queryset_list, 10)
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    context = {
        "object_list": queryset,
        "title": "Записи:",
        "today": today,
        'tag': tag,
    }
    return render(request, "post_list.html", context)


def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=instance
    )
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save_m2m()
        messages.success(request, "Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Deleted")
    return redirect("posts:list")


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contacts(request):
    return render(request, "contacts.html")
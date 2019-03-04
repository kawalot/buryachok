from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Category

def recipes_list(request, slug_category=None):
    
    queryset_list = Recipe.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) |
            Q(author__last_name__icontains=query)
        ).distinct()

    if slug_category:
        list_by_category = get_object_or_404(Category, slug=slug_category)
        print("list by category = ", list_by_category)
        queryset_list = queryset_list.filter(category__slug__exact=slug_category)
        print("queryset = ", queryset_list)
    context = {
        "object_list": queryset_list,
        "slug": list_by_category,
    }
    # paginator = Paginator(queryset_list, 10)
    # page = request.GET.get('page')
    # queryset = paginator.get_page(page)
    # context = {
    #     "object_list": queryset,
    #     "title": "Записи:",
    #     "today": today,
    #     'tag': tag,
    # }
    return render(request, "recipes_list.html", context)


def recipe_detail(request, slug=None):
    instance = get_object_or_404(Recipe, slug=slug)

    context = {
        "object": instance,
    }
    return render(request, "recipe_detail.html", context)
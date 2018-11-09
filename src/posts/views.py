
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
# Create your views here.


def post_create(request):
	return HttpResponse("<h1>Hello from Docker</h1>")

def post_detail(request):
	context = {
		"title": "detail"
	}
	return render(request, "index.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list": queryset,
		"title": "list"
	}
	return render(request, "index.html", context)
	#return HttpResponse("<h1>Hello from Docker</h1>")

def post_update(request):
	return HttpResponse("<h1>Hello from Docker</h1>")

def post_delete(request):
	
	return HttpResponse("<h1>Hello from Docker</h1>")
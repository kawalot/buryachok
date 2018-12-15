from django.contrib import admin
from django.urls import path
from posts import views

from .views import (
		post_list,
		post_detail,
		post_create,
		post_update,
		post_delete,
	)

app_name = "posts"

urlpatterns = [
	path('', post_list, name='list'),
    path('tag/<slug:tag_slug>/', post_list, name='list_by_tag'),
    path('create/', post_create),
    path('<slug:slug>/', post_detail, name='detail'),
    path('<slug:slug>/edit/', post_update, name='update'),
    path('<slug:slug>/delete/', post_delete),
]
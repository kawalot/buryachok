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
    path('create/', post_create),
    path('<id>/', post_detail, name='detail'),
    path('<id>/edit/', post_update, name='update'),
    path('<id>/delete/', post_delete),
]
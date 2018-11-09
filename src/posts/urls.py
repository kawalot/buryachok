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

urlpatterns = [
    path('', post_list),
    path('create/', post_create),
    path('detail/', post_detail),
    path('update/', post_update),
    path('delete/', post_delete),
]
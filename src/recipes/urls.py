from django.urls import path
from .views import recipes_list, recipe_detail

app_name = "recipes"

urlpatterns = [
    path('', recipes_list, name='recipes_list'),

    path('<slug:slug>/', recipe_detail, name='recipe_detail'),
    # path('tag/<slug:tag_slug>/', post_list, name='list_by_tag'),
    # path('create/', post_create),
    # path('<slug:slug>/', post_detail, name='detail'),
    # path('<slug:slug>/edit/', post_update, name='update'),
    # path('<slug:slug>/delete/', post_delete),
]

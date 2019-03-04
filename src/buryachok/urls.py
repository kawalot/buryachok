"""buryachok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts import views
from recipes import views as recipes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include("posts.urls", namespace='posts')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home, name='home_page'),
    path('about/', views.about, name='about_page'),
    path('contacts/', views.contacts, name='contacts_page'),
    path('recipes/', include("recipes.urls", namespace='resipes')),
    path('category/<slug:slug_category>/', recipes_views.recipes_list, name='recipes_list_by_category'),    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
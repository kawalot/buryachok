from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from taggit.managers import TaggableManager


def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" %(instance.id, filename, extension)
    return "%s/%s" % (instance.id, filename)


class Category(models.Model):
    """
    A model class describing a category.
    """
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("recipes_list_by_category", kwargs={"slug": self.slug})

class Recipe(models.Model):
    """
    A model describing a recipe.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(
        upload_to="uploads/recipe_photos",
        null=True,
        blank=True,
    )
    content = RichTextUploadingField(blank=True, null=True)
    category = models.ManyToManyField(Category, verbose_name='Categories')
    publish = models.DateField(auto_now=False, auto_now_add=False)
    tags = TaggableManager(blank=True)
    
    class Meta:
        ordering = ["-publish", "-title"]
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:recipe_detail", kwargs={"slug": self.slug})
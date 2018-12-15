from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Post
        fields = [
            "title",
            "tags",
            "content",
            "image",
            "draft",
            "publish",
        ]
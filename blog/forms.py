from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'category', 'featured_image', 'excerpt', 'content', 'opinion',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'choice')


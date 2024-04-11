from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Opinions(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Choices(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True, max_length=200)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="categories"
    )
    opinion = models.ForeignKey(
        Opinions, on_delete=models.CASCADE, related_name="opinions"
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField(default="johndoe@example.com")
    body = models.TextField()
    choice = models.ForeignKey(
        Choices, on_delete=models.CASCADE, related_name="choices"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

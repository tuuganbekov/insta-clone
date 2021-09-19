from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='authors', null=True
                               )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}--{self.id}"


class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='insta_projects/')
    post = models.ForeignKey(
        Post, related_name='post',
        on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.image.url}"


class HashTag(models.Model):
    title = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField(blank=True)
    author = models.ForeignKey(
                                User, on_delete=models.CASCADE,
                                related_name='author', null=True
                               )
    post = models.ForeignKey(Post, related_name='posts', on_delete=models.CASCADE)

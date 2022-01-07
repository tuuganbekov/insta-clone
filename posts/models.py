from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    post_image = models.ImageField(upload_to='media/posts/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='authors', null=True
                               )
    liked_users = models.ManyToManyField(User, related_name='liked_post')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}--{self.id}"


class Comment(models.Model):
    text = models.TextField(blank=True)
    author = models.ForeignKey(
                                User, on_delete=models.CASCADE,
                                related_name='author', null=True
                               )
    post = models.ForeignKey(Post, related_name='post_comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username} - {self.text}"


class Like(models.Model):
    quantity = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username} {self.post.title}"

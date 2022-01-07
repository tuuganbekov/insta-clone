from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    info = models.TextField(verbose_name='Info about you', null=True, blank=True)
    profile_image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    friends_list = models.ManyToManyField('User', related_name='friends', blank=True)

    def __str__(self):
        return f'{self.username}'

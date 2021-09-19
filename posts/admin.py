from django.contrib import admin
from posts.models import Post, Image, HashTag, Comment


# Register your models here.
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(HashTag)
admin.site.register(Comment)
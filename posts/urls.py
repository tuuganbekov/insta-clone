from django.urls import path

from posts.views import post_new

app_name = 'posts'

urlpatterns = [
    path('create/', post_new, name='add_post'),
]

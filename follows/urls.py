from django.urls import path

from follows.views import display_followers

app_name = 'follows'

urlpatterns = [
    path('', display_followers, name='index'),
]

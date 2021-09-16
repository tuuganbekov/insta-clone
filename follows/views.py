from django.shortcuts import render
from follows.models import Followings
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your views here.
def display_followers(request):
    current_user = request.user
    follows = Followings.objects.filter(from_user=current_user.id)

    return render(request, 'followers/followers.html', locals())

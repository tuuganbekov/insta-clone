from random import shuffle
from itertools import chain
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
# from users.decorators import unauthenticated_user

from users.forms import CreateUserForm
from posts.models import Post


User = get_user_model()


# Create your views here.
# @unauthenticated_user
def register_page(request):
    form = CreateUserForm

    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.profile_image = form.cleaned_data['profile_image']
            user.save()
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'accounts/register.html', locals())


# @unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:index')
    context = {}
    return render(request, 'accounts/login.html', locals())


def logout_user(request):
    logout(request)
    return redirect('users:login')


@login_required(login_url='users:login')
def index(request):
    current_user = request.user
    friends = current_user.friends_list.all()
    my_posts = Post.objects.filter(author=current_user).order_by('-created_date')
    friends_posts = Post.objects.filter(author__in=friends).order_by('-created_date')
    all_posts = list(chain(friends_posts, my_posts))
    posts = []
    for p in all_posts:
        posts.append({
                        "is_user_liked": True,
                        "post": p,
                        "count": p.liked_users.all().count()
                     })
    # shuffle(posts)
    return render(request, 'index.html', locals())


@login_required(login_url='users:login')
def cabinet(request):
    user = User.objects.get(id=request.user.id)
    followings = user.friends_list.count()
    followers = user.friends.all().count()
    posts = Post.objects.filter(author=request.user)
    return render(request, 'accounts/cabinet.html', locals())


@login_required(login_url='users:login')
def profile(request, id):
    user = User.objects.get(id=id)
    is_friend = False
    followings = user.friends_list.count()
    followers = user.friends.all().count()
    posts = Post.objects.filter(author=user)
    if request.user.friends_list.filter(id=user.id).exists():
        is_friend = True
    return render(request, 'accounts/profile.html', locals())


def follow_operation(request, id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        if 'follow' in request.POST.keys():
            request.user.friends_list.add(user)
        else:
            request.user.friends_list.remove(user)
    return redirect('users:profile', id=user.id)


# Search view
def search_users(request):
    if request.method == 'POST':
        searched = request.POST['search-users']
        users = User.objects.filter(username__contains=searched)
        return render(request, 'accounts/search_results.html', locals())
    return render(request, 'accounts/search_results.html', locals())
















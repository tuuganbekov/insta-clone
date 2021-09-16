from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.forms import CreateUserForm


# Create your views here.
def register_page(request):
    if request.user.is_authenticated:
        return redirect('users:index')
    else:
        form = CreateUserForm

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('users:login')

        context = {'form': form}
        return render(request, 'accounts/register.html', locals())


def login_page(request):
    if request.user.is_authenticated:
        return redirect('users:index')
    else:
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
    context = {}
    return render(request, 'index.html', locals())


@login_required(login_url='users:login')
def cabinet(request):
    user = request.user
    return render(request, 'accounts/cabinet.html', locals())

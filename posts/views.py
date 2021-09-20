from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from posts.models import Post
from posts.form import PostForm


# Create your views here.
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.post_image = form.cleaned_data['post_image']
            post.updated_date = timezone.now()
            post.save()
            return redirect('users:index')
    else:
        form = PostForm()

    return render(request, 'posts/post_edit.html', locals())


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('users:index')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', locals())

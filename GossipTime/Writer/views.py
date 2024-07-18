from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', category_slug=post.category.slug, pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'Writer/create_post.html', {'form': form})


def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'Writer/create_post.html', {'form': form, 'type': 'update'})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        post.is_delete = True
        post.delete_date = timezone.now()
        post.save()
        return redirect('post_list')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Main/blog-category.html', {'posts': posts})

def news(request):
    return render(request, 'Writer/news.html')



@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('post_detail', category_slug=post.category.slug, pk=post.pk)

@login_required
def dislike(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    dislike, created = Dislike.objects.get_or_create(user=request.user, post=post)
    if not created:
        dislike.delete()
    return redirect('post_detail', category_slug=post.category.slug, pk=post.pk)

def fashion_list(request):
    fashions = Post.objects.filter(category__slug='fashion')
    return render(request, 'Main/fashion.html', {'fashions': fashions})

def post_detail(request, category_slug, pk):
    post = get_object_or_404(Post, category__slug=category_slug, pk=pk)
    return render(request, 'Main/post_detail.html', {'post': post})

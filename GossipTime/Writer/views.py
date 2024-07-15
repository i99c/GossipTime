from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import datetime

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    
    return render(request, 'Writer/create_post.html', {'form': form, 'type': 'create'})

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
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
        return redirect('post:base')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Main/blog-category.html', {'posts': posts})

def news(request):
    return render(request, 'Writer/news.html')

def news_detail(request, post_id):  # Yeni eklenen görünüm fonksiyonu
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'Writer/news_detail.html', {'post': post})

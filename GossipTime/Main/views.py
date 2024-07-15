from django.shortcuts import render, get_object_or_404
from .models import *
from Writer.models import Post

def index(request):
    return render(request, 'Main/index.html')

def blog(request):
    return render(request, 'Main/blog.html')

def blog_category(request):
    return render(request, 'Main/blog-category.html')

def fashion(request):
    fashion_posts = Post.objects.filter(category__name='Fashion').exclude(pk__isnull=True)
    return render(request, 'Main/fashion.html', {'fashions': fashion_posts})

def lifestyle(request):
    lifestyle_post = Post.objects.filter(category__name='Lifestyle').exclude(pk__isnull=True)
    return render(request, 'Main/lifestyle.html', {'lifestyles':lifestyle_post})

def travel(request):
    travel_post = Post.objects.filter(category__name='Travel').exclude(pk__isnull=True)
    return render(request, 'Main/travel.html', {'travels':travel_post})

def post_single(request):
    return render(request, 'Main/post-single.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post-single.html', {'post': post})


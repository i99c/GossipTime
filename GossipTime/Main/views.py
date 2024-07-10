from django.shortcuts import render
from .models import *
from Writer.models import Post

def index(request):
     return render(request, 'Main/base.html')

def blog(request):
    return render(request, 'Main/blog.html')

def blog_category(request):
    return render(request, 'Main/blog-category.html')

def fashion(request):
    fashion_posts = Post.objects.filter(category__name='Fashion')
    return render(request, 'Main/fashion.html', {'fashions': fashion_posts})

def lifestyle(request):
    lifestyle_post = Post.objects.filter(category__name='Lifestyle')
    return render(request, 'Main/lifestyle.html', {'lifestyles':lifestyle_post})

def travel(request):
    travel_post = Post.objects.filter(category__name='Travel')
    return render(request, 'Main/travel.html', {'travels':travel_post})

def post_single(request):
    return render(request, 'Main/post-single.html')

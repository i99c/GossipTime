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
    articles = Post.objects.all()  # Tüm makaleleri almak için örnek bir sorgu
    context = {
        'articles': articles,
    }
    return render(request, 'Main/post-single.html', context)

def post_detail(request, category_slug, pk):
   
    post = get_object_or_404(Post, category__slug=category_slug, pk=pk)

    # Template'e gönderin
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)

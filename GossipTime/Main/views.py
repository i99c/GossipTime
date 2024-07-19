from django.shortcuts import render, get_object_or_404
from .models import *
from Writer.models import Post
from django.db.models import Count

def index(request):
    latest_post = Post.objects.all().order_by('-created_date').first()
    second_latest_post = Post.objects.all().order_by('-created_date')[1] if Post.objects.count() > 1 else None
    most_liked_post = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes').first()
    return render(request, 'Main/index.html', {
        'latest_post': latest_post,
        'second_latest_post': second_latest_post,
        'most_liked_post': most_liked_post  # most_liked_post eklenmiş
    })

def most_liked_post_view(request):
    # En çok beğenilen gönderiyi al
    most_liked_post = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes').first()
    return render(request, 'Main/partials/__articleright.html', {'most_liked_post': most_liked_post})


def blog(request):
    return render(request, 'Main/blog.html')

def blog_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'Main/blog-category.html', {'posts': posts, 'category': category})


def fashion(request):
    fashion_posts = Post.objects.filter(category__name='Fashion')
    return render(request, 'Main/fashion.html', {'fashions': fashion_posts})

def lifestyle(request):
    lifestyle_posts = Post.objects.filter(category__name='Lifestyle')
    return render(request, 'Main/lifestyle.html', {'lifestyles': lifestyle_posts})

def travel(request):
    travel_posts = Post.objects.filter(category__name='Travel')
    return render(request, 'Main/travel.html', {'travels': travel_posts})

def post_single(request):
    articles = Post.objects.all()  # Tüm makaleleri almak için örnek bir sorgu
    context = {
        'articles': articles,
    }
    return render(request, 'Main/post-single.html', context)

def post_detail(request, slug, id):
    category=get_object_or_404(Category, slug=slug)
    post = get_object_or_404(Post, id=id, category=category)
    return render(request, 'Main/post-single.html', {'post': post})


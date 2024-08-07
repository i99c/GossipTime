from django.shortcuts import render, get_object_or_404
from .models import *
from Writer.models import *
from django.db.models import Count


def index(request):
    posts = Post.objects.filter(category__isnull=False).order_by('-created_date')
    
    latest_post = posts.first()
    second_latest_post = posts[1] if posts.count() > 1 else None
    third_latest_post = posts[2] if posts.count() > 2 else None
    fourth_latest_post = posts[3] if posts.count() > 3 else None
    most_liked_post = Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes').first()
    most_viewed_posts = Post.objects.order_by('-view_count')[:3]
    oldest_posts = Post.objects.order_by('created_date')[:9]

    return render(request, 'Main/index.html', {
        'latest_post': latest_post,
        'second_latest_post': second_latest_post,
        'third_latest_post': third_latest_post,
        'fourth_latest_post': fourth_latest_post,
        'most_liked_post': most_liked_post,
        'most_viewed_posts': most_viewed_posts,
        'oldest_posts': oldest_posts
    })

def oldest_posts(request):
    # En eski gönderileri almak için
    posts = Post.objects.filter(category__isnull=False).order_by('created_date')
    
    # En eski 12 gönderiyi çekiyoruz ve her kategoriden 3'er tane olacak şekilde sınırlıyoruz
    oldest_posts = {
        'travel': posts.filter(category='travel')[:3],
        'fashion': posts.filter(category='fashion')[:3],
        'lifestyle': posts.filter(category='lifestyle')[:3],
    }

    return render(request, 'Main/oldest_posts.html', {
        'oldest_posts': oldest_posts,
    })

def most_liked_post_view(request):
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
    category = get_object_or_404(Category, slug=slug)
    post = get_object_or_404(Post, id=id, category=category)
    post.view_count += 1 
    post.save()
    return render(request, 'Main/post-single.html', {'post': post})

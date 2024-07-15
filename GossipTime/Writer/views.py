from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm
from .models import Post




def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Your redirect URL here
    else:
        form = PostForm()
    
    return render(request, 'Writer/create_post.html', {'form': form})  # Doğru template yolunu kullanın






def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Main/blog-category.html', {'posts': posts})


def news(request):
    return render(request, 'Writer/news.html')


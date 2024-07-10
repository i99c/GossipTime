from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm
from .models import Post



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Replace 'post_list' with the name of your post list view
    else:
        form = PostForm()
    return render(request, 'Writer/create_post.html', {'form': form})

# Create your views here.




def post_list(request):
    posts = Post.objects.all()
    return render(request, 'Main/blog-category.html', {'posts': posts})




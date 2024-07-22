from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from Writer.forms import *
import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def writerdashboard(request):
    user = request.user
    posts = Post.objects.filter(user=user)  # Assuming `user` is the field in the Post model
    return render(request, 'writer-dashboard.html', {'posts': posts})
    
def readerdashboard(request):
    return render(request, 'reader-dashboard.html')

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
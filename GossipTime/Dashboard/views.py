from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from Writer.forms import *
import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

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

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})

@csrf_exempt
def profile_update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        profile = get_object_or_404(Profile, user=request.user)
        profile.subtitle = data.get('subtitle')
        profile.title = data.get('title')
        profile.bio = data.get('bio')
        profile.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})
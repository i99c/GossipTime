from django.shortcuts import render, redirect, get_object_or_404
from .models import * # Eğer tüm modelleri almak yerine belirli modelleri almak daha iyidir.
import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from Writer.models import * # Eğer tüm modelleri almak yerine belirli modelleri almak daha iyidir.


@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('post_detail', category_slug=post.category.slug, pk=post.pk)

@login_required
def dislike(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    dislike, created = Dislike.objects.get_or_create(user=request.user, post=post)
    if not created:
        dislike.delete()
    return redirect('post_detail', category_slug=post.category.slug, pk=post.pk)
from django.urls import path
from .views import *
from Writer.views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog_category/<slug:slug>/', blog_category, name='blog-category'),
    path('fashion/', fashion, name='fashion'),
    path('lifestyle/', lifestyle, name='lifestyle'),
    path('travel/', travel, name='travel'),
    path('post/<slug:slug>/<int:id>/', post_detail, name='post-detail'),
    path('most-liked/', most_liked_post_view, name='most-liked-post'),
    
]
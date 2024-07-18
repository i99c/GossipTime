from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog/', blog, name='blog'),
    path('blog_category/', blog_category, name='blog-category'),
    path('fashion/', fashion, name='fashion'),
    path('lifestyle/', lifestyle, name='lifestyle'),
    path('travel/', travel, name='travel'),
    path('post-single/', post_single, name='post-single'),
    path('fashion/<int:id>/', fashion_detail, name='fashion-detail'),
    path('lifestyle/<int:id>/', lifestyle_detail, name='lifestyle-detail'),
    path('travel/<int:id>/', travel_detail, name='travel-detail'),
 

 ]

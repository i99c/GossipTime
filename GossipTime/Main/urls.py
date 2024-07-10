from django.urls import path
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', index, name='Main/base'),
    path('blog/', blog, name='Main/blog'),
    path('blog_category/', blog_category, name='Main/blog-category'),
    path('fashion/', fashion, name='Main/fashion'),
    path('lifestyle/', lifestyle, name='Main/lifestyle'),
    path('travel/', travel, name='Main/travel'),
    path('post_single/', post_single, name='Main/post-single'),
]

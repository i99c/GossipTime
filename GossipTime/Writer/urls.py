from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('create/',create_post, name='create_post'),   
    path('', post_list, name='post_list'),  # Burada post_list isimli bir URL tanımlanıyor
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

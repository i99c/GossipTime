from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register_view, name='register'),
    path('ana-base/', views.base, name='main/base'),
    path('logout/', views.logout_view, name='logout'),  # Doğru fonksiyon adı
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register_view, name='register'),
    path('ana-base', views.base, name='main/base'),
    path('ana-base/', views.base, name='main/base'),  # Doğru görünüm adı ile değiştirin
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

from django.urls import path
from .views import *
from Login.views import *
from Writer.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('writer-dashboard/',writerdashboard, name='writerdashboard' ),
    path('reader-dashboard/', readerdashboard, name='readerdashboard'),
    path('update/<str:post_id>/', update_post, name='update_post'),   
    path('user-dashboard/', user_dashboard, name='user_dashboard'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

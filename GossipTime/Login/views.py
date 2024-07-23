from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import Writer, Reader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect

def login(request):
    if request.method == 'POST':
        login_info = request.POST.get('username_or_email')
        password = request.POST.get('password')
        
        if not login_info or not password:
            messages.error(request, 'Kullanıcı adı ve şifre gereklidir.')
            return render(request, 'Login/login.html')

        user = None
        if '@' in login_info:
            # E-posta ile giriş yapma 
            try:
                user = User.objects.get(email=login_info)
            except User.DoesNotExist:
                messages.error(request, 'Kullanıcı bulunamadı!')
                return render(request, 'Login/login.html')
        else:
            # Kullanıcı adı ile giriş yapma
            user = authenticate(request, username=login_info, password=password)

        if user is not None and user.check_password(password):
            if user.is_superuser:
                # Admin kullanıcısını atla
                auth_login(request, user)
                return redirect('/admin/')
            else:
                try:
                    writer = Writer.objects.get(user=user)
                    auth_login(request, user)
                    return redirect("writerdashboard")
                except Writer.DoesNotExist:
                    try:
                        reader = Reader.objects.get(user=user)
                        auth_login(request, user)
                        return redirect("readerdashboard")
                    except Reader.DoesNotExist:
                        messages.error(request, 'Kullanıcı mevcut ancak Okur veya Yazar değil.')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre yanlış!')

    return render(request, 'Login/login.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            messages.error(request, 'Şifreler eşleşmiyor!')
            return render(request, 'Login/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Kullanıcı adı zaten mevcut!')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email zaten mevcut!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            Reader.objects.create(user=user, phone=phone)
            auth_login(request, user)
            return redirect('login')  # Kayıt başarılıysa login sayfasına yönlendir.

    return render(request, 'Login/register.html')

@login_required
def user_dashboard(request):
    user = request.user

    try:
        Writer.objects.get(user=user)
        return redirect('writerdashboard')
    except Writer.DoesNotExist:
        try:
            Reader.objects.get(user=user)
            return redirect('readerdashboard')
        except Reader.DoesNotExist:
            return redirect('login')  # Eğer kullanıcı ne Writer ne de Reader ise login sayfasına yönlendir.

def base(request):
    return render(request, 'base.html')


def logout_view(request):
    logout(request)
    return redirect('login')  # Kullanıcıyı giriş sayfasına yönlendirir
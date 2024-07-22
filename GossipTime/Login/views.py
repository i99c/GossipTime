from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import Writer, Reader
from django.contrib import messages
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        login_info = request.POST.get('username_or_email')
        password = request.POST.get('password')
        
        if not login_info or not password:
            messages.error(request, 'Kullanıcı adı ve şifre gereklidir.')
            return render(request, 'Login/login.html')
        
        try:
            user_mail = User.objects.get(email=login_info)
            user = authenticate(request, username=user_mail.username, password=password)
        except User.DoesNotExist:
            user = authenticate(request, username=login_info, password=password)
        
        if user is not None:
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
        
        # Başarısız giriş denemesi için render işlemi burada
        return render(request, 'Login/login.html', {'messages': messages})
    else:
        return render(request, 'Login/login.html', {'messages': messages})

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')  # Şifre tekrarı alanının adını kontrol edin

    
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Kullanıcı adı zaten mevcut!')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email zaten mevcut!')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                # Örneğin Reader modelini kullanıyorsanız
                reader = Reader.objects.create(user=user, phone=phone)
                reader.save()
                auth_login(request, user)
                return redirect('login')  # Kayıt başarılıysa yönlendirilecek sayfa
        else:
            messages.error(request, 'Şifreler eşleşmiyor!')
    
    return render(request, 'login/login.html')

def base(request):
    return render(request, 'main/base.html')


def user_dashboard(request):
    user = request.user
    
    try:
        writer = Writer.objects.get(user=user)
        return redirect('writerdashboard')
    except Writer.DoesNotExist:
        try:
            reader = Reader.objects.get(user=user)
            return redirect('readerdashboard')
        except Reader.DoesNotExist:
            return redirect('login')  # Eğer kullanıcı ne Writer ne de Reader ise login sayfasına yönlendir.
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.

# Register Akun Baru
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Password Check
        if password == password2:
            # Username Check
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username telah digunakan')
                return redirect('register')
            else:
                # Email Check
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email telah terdaftar')
                    return redirect('register')
                else:
                    # Register New user
                    user = User.objects.create_user(username=username, 
                                                    password=password, 
                                                    email=email, 
                                                    first_name=first_name, 
                                                    last_name=last_name)
                    # auth.login(request, user)
                    # messages.success(request, 'Anda Telah Terdaftar')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Anda Telah Terdaftar')
                    return redirect('login')
        else:
            messages.error(request, 'Password tidak sama')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
            messages.success(request, 'Berhasil Login')
        else:
            messages.error(request, 'Username atau Password Salah')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Anda telah Logout')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
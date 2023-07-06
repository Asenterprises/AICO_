```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'dashboard.html')

def production_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'production.html')

def quality_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'quality.html')

def warehouse_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'warehouse.html')
```
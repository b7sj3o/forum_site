from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Неправильний логін чи пароль. Спробуйте знову'))
            return redirect('login')
    else:
        return render(request, 'forum_members/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ('Ви вийшли з акаунту'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Ви успішно зареєструвались')
            return redirect('home')

    else:
        form = RegisterUserForm()
    
    return render(request, 'forum_members/register.html', {'form': form})
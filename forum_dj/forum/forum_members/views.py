from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(
                request, ('Неправильний логін чи пароль. Спробуйте знову'))
            return redirect('login')
    else:
        return render(request, 'forum_members/login.html', {})


def logout_user(request):
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)
    messages.success(request, ('Ви вийшли з акаунту'))
    return redirect('home')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'forum_members/register.html', {'form': form})

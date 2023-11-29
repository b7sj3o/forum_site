from django.shortcuts import render, redirect
from .models import Advertisements, MainPictureBanner, MainTextBanner, UserData, ThemeMessage, Themes, SandboxMessage, User
from django.contrib.auth.decorators import login_required
import random
from .forms import UserForm
from django.db.models import Q


# -------------- RENDER --------------


def index(request):
    advertisements = Advertisements.objects.all().order_by('-id')

    try:
        chosen_product = MainTextBanner.objects.get()
        main_banners = MainPictureBanner.objects.all()
        main_banner = random.choice(main_banners)
    except:
        chosen_product = None
        main_banner = None

    last_messages = SandboxMessage.objects.all().order_by('-id')[:5]
    return render(request, 'forum_pages/index.html', {
        'advertisements': advertisements,
        'chosen_product': chosen_product,
        'main_banner': main_banner,
        'last_messages': last_messages
    })


def sandbox(request):
    messages = SandboxMessage.objects.all().order_by('-created')

    if request.method == 'POST':
        message = SandboxMessage.objects.create(
            user=request.user,
            main_text=request.POST.get('main_text')
        )
        return redirect('sandbox')

    context = {'messages': messages}
    return render(request, 'forum_pages/sandbox.html', context)


def themes(request):
    themes = Themes.objects.all().order_by('-created')
    context = {'themes': themes}
    return render(request, 'forum_pages/themes.html', context)


def theme(request, user, pk):
    room = Themes.objects.get(id=pk)
    room_messages = room.thememessage_set.all().order_by('-id')

    if request.method == 'POST':
        theme = ThemeMessage.objects.create(
            user=request.user,
            theme=room,
            main_text=request.POST.get('main_text')
        )
        return redirect('theme', user=request.user, pk=room.id)

    context = {'room_messages': room_messages, 'room': room}
    return render(request, 'forum_pages/theme.html', context)


def createTheme(request):
    if request.method == "POST":
        theme = Themes.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            main_text=request.POST.get('main_text')
        )
        return redirect('themes')
    context = {}
    return render(request, 'forum_pages/create-theme.html', context)

def createAdvertisment(request):
    if request.method == "POST":
            advert = Advertisements.objects.create(
                name=request.user,
                title=request.POST.get('title'),
                text=request.POST.get('main_text')
            )
            return redirect('home')
    context = {}
    return render(request, 'forum_pages/create-advertisment.html', context)


def deleteMessage(request, pk):
    referer = request.META.get('HTTP_REFERER', None)
    if 'sandbox' in referer:
        message = SandboxMessage.objects.get(id=pk)
    else:
        message = ThemeMessage.objects.get(id=pk)
    message.delete()

    return redirect(referer)


def deleteTheme(request, pk):
    theme = Themes.objects.get(id=pk)
    theme.delete()

    return redirect('themes')


def userProfile(request, pk):
    user = User.objects.get(username=pk)
    cuser = user
    user_messages = len(Themes.objects.filter(user=user))

    last_themes = ThemeMessage.objects.filter(user=user).order_by('-created')
    messages_amount = len(last_themes)

    user_forms = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=request.user.username)
        # else:
            # return redirect('home')
        

    context = {
        'cuser': cuser,
        'user_messages': user_messages,
        'user_forms': user_forms,
        'last_themes': last_themes,
        'messages_amount': messages_amount
    }
    return render(request, 'forum_pages/user-profile.html', context)


def search(request):
    q = request.GET.get('q', '')
    keywords = q.split()

    query = Q()

    for keyword in keywords:
        query |= Q(title__icontains=keyword) | Q(main_text__icontains=keyword)

    themes = Themes.objects.filter(query).order_by('-created')

    themes_count = themes.count()
    if not themes_count:
        themes_count = 0

    context = {
        'themes': themes,
        'themes_count': themes_count,
        'is_searched': True
    }

    return render(request, 'forum_pages/themes.html', context)

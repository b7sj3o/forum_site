from django.shortcuts import render, redirect
from .models import Advertisements, MainPictureBanner, MainTextBanner, UserData, ThemeMessage, Themes, SandboxMessage
from django.contrib.auth.decorators import login_required
import random

# -------------- RENDER --------------


def index(request):
    advertisements = Advertisements.objects.all().order_by('-id')
    chosen_product = MainTextBanner.objects.get()

    main_banners = MainPictureBanner.objects.all()
    main_banner = random.choice(main_banners)

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

    if request.method == 'POST':
        theme = Themes.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            main_text=request.POST.get('main_text')
        )
        return redirect('themes')

    context = {'themes': themes}
    return render(request, 'forum_pages/themes.html', context)


def theme(request, pk):
    room = Themes.objects.get(id=pk)
    room_messages = room.thememessage_set.all().order_by('-id')

    if request.method == 'POST':
        theme = ThemeMessage.objects.create(
            user=request.user,
            theme=room,
            main_text=request.POST.get('main_text')
        )
        return redirect('theme', pk=room.id)

    context = {'room_messages': room_messages, 'room': room}
    return render(request, 'forum_pages/theme.html', context)


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
from django.shortcuts import render, redirect
from .models import Advertisements, MainPictureBanner, MainTextBanner, UserData, SubThemeMessage, Themes, SandboxMessage, User, SubThemes
from django.contrib.auth.decorators import login_required
import random
from .forms import UserForm
from django.db.models import Q


# -------------- RENDER --------------


def index(request):
    advertisements = Advertisements.objects.all().order_by('-id')
    themes = Themes.objects.all().order_by('-id')

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
        'last_messages': last_messages,
        'themes': themes
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


def allThemes(request):
    themes = Themes.objects.all().order_by('-id')

    context = {
        'themes': themes
    }
    return render(request, 'forum_pages/allThemes.html', context)


def subThemes(request, pk):
    theme = Themes.objects.get(id=pk)
    subthemes = theme.subthemes.all().order_by('-id')
    for subtheme in subthemes:
        print(subtheme.id)
    # theme = Themes.objects.get(id=pk)
    context = {
        'theme': theme,
        'subthemes': subthemes,
    }
    return render(request, 'forum_pages/subThemes.html', context)


def subTheme(request, user, pk):
    room = SubThemes.objects.get(id=pk)
    room_messages = room.subtheme_messages.all().order_by('-id')

    if request.method == 'POST':
        theme = SubThemeMessage.objects.create(
            user=request.user,
            subtheme=room,
            main_text=request.POST.get('main_text')
        )
        return redirect('subtheme', user=room.user, pk=room.id)

    context = {'room_messages': room_messages, 'room': room}
    return render(request, 'forum_pages/subTheme.html', context)


def createSubTheme(request, topic_id):
    base_theme = Themes.objects.get(pk=topic_id)
    if request.method == "POST":
        theme = SubThemes.objects.create(
            user=request.user,
            base_theme=base_theme,
            title=request.POST.get('title'),
            main_text=request.POST.get('main_text')
        )
        return redirect('subthemes', pk=topic_id)
    context = {}
    return render(request, 'forum_pages/create-theme.html', context)


def deleteSubTheme(request, pk):
    referer = request.META.get('HTTP_REFERER', None)

    subtheme = SubThemes.objects.get(id=pk)
    subtheme.delete()

    return redirect(referer)


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
        message = SubThemeMessage.objects.get(id=pk)
    message.delete()

    return redirect(referer)


def userProfile(request, pk):
    user = User.objects.get(username=pk)
    cuser = user
    user_messages = len(SubThemes.objects.filter(user=user))

    last_themes = SubThemeMessage.objects.filter(
        user=user).order_by('-created')
    messages_amount = len(last_themes)

    user_forms = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.username)
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

    subthemes = SubThemes.objects.filter(query).order_by('-created')

    context = {
        'subthemes': subthemes,
        'is_searched': True,
        'requested_words': q
    }

    return render(request, 'forum_pages/subThemes.html', context)

def advertPage(request):
    context={}
    return render(request, 'forum_pages/advertisment.html', context)
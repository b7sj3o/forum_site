from django.shortcuts import render, redirect
from .models import Advertisements, MainPictureBanner, MainTextBanner, UserData, SubThemeMessage, Themes, SandboxMessage, User, SubThemes
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.db.models import Q


# -------------- RENDER --------------


def index(request):
    advertisements = Advertisements.objects.all().order_by('-id')
    themes = Themes.objects.all().order_by('-id')

    try:
        chosen_product = MainTextBanner.objects.get()
        main_banner = MainPictureBanner.objects.all()[0]
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


def sandbox(request, page):
    referer = request.META.get('HTTP_REFERER', None)
    if page < 1:
        return redirect(referer)

    messages = SandboxMessage.objects.all().order_by('-created')
    messages_per_page = messages[page*10-10:page*10]

    main_banner = MainPictureBanner.objects.all()[0]

    pages_amount = len(messages) // 10 if len(messages) % 10 == 0 else len(messages) // 10 + 1
    pages_list_amount = [x for x in range(1, pages_amount+1)]

    if page > pages_amount:
        return redirect(referer)

    if request.method == 'POST':
        message = SandboxMessage.objects.create(
            user=request.user,
            main_text=request.POST.get('main_text')
        )
        return redirect('sandbox', page=page)

    context = {
        'messages': messages_per_page,
        'main_banner': main_banner,
        'pages_amount': pages_list_amount,
        'current_page': page
    }
    return render(request, 'forum_pages/sandbox.html', context)


def allThemes(request):
    themes = Themes.objects.all().order_by('-id')

    context = {
        'themes': themes
    }
    return render(request, 'forum_pages/allThemes.html', context)


def subThemes(request, pk, page):
    page = int(page)
    referer = request.META.get('HTTP_REFERER', None)
    if page < 1:
        return redirect(referer)
    
    theme = Themes.objects.get(id=pk)
    subthemes = theme.subthemes.all().order_by('-id')
    subthemes_per_page = subthemes[page*10-10:page*10]


    pages_amount = len(
        subthemes) // 10 if len(subthemes) % 10 == 0 else len(subthemes) // 10 + 1
    pages_list_amount = [x for x in range(1, pages_amount+1)]

    if page > pages_amount and pages_amount:
        return redirect(referer)

    context = {
        'theme': theme,
        'subthemes': subthemes_per_page,
        'pages_amount': pages_list_amount,
        'current_page': page,
        'pk': pk
    }
    return render(request, 'forum_pages/subThemes.html', context)


def SearchedsubThemes(request, page, q):
    referer = request.META.get('HTTP_REFERER', None)
    if page < 1:
        return redirect(referer)


    keywords = q.split()
    query = Q()
    for keyword in keywords:
        query |= Q(title__icontains=keyword) | Q(main_text__icontains=keyword)
    subthemes = SubThemes.objects.filter(query).order_by('-created')

    any_result = True if not len(subthemes) else False

    subthemes_per_page = subthemes[page*10-10:page*10]
    pages_amount = len(subthemes) // 10 if len(subthemes) % 10 == 0 else len(subthemes) // 10 + 1
    pages_list_amount = [x for x in range(1, pages_amount+1)]

    if page > pages_amount and pages_amount:
        return redirect(referer)

    context = {
        'subthemes': subthemes_per_page,
        'pages_amount': pages_list_amount,
        'current_page': page,
        'any_result': any_result,
        'requested_words': q
    }
    return render(request, 'forum_pages/searched-subthemes.html', context)


def subTheme(request, pk, page):
    referer = request.META.get('HTTP_REFERER', None)
    if page < 1:
        return redirect(referer)

    room = SubThemes.objects.get(id=pk)
    room_messages = room.subtheme_messages.all().order_by('-id')

    messages_per_page = room_messages[page*10-10:page*10]

    if not messages_per_page:
        pages_amount = 1
    else:
        pages_amount = len(room_messages) // 10 if len(room_messages) % 10 == 0 else len(room_messages) // 10 + 1

    pages_list_amount = [x for x in range(1, pages_amount+1)]
    if page > pages_amount and pages_amount:
        return redirect(referer)


    if request.method == 'POST':
        theme = SubThemeMessage.objects.create(
            user=request.user,
            subtheme=room,
            main_text=request.POST.get('main_text')
        )
        return redirect('subtheme', pk=pk, page=page)

    context = {
        'room_messages': messages_per_page,
        'room': room,
        'pk': pk,
        'pages_amount': pages_list_amount,
        'current_page': page
    }
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
        return redirect('subthemes', pk=topic_id, page=1)
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

    context = {
        'cuser': cuser,
        'user_messages': user_messages,
        'user_forms': user_forms,
        'last_themes': last_themes,
        'messages_amount': messages_amount
    }
    return render(request, 'forum_pages/user-profile.html', context)


def search(request):
    q = request.GET.get('q')
    if not q:
        return redirect(request.META.get('HTTP_REFERER', None))
    return redirect('searched-subthemes', page=1, q=q) 


def advertPage(request):
    context = {}
    return render(request, 'forum_pages/advertisment.html', context)


def updateMessage(request, pk, mes, page):
    room = SubThemes.objects.get(id=pk)
    room_messages = room.subtheme_messages.all().order_by('-id')

    messages_per_page = room_messages[page*10-10:page*10]
    pages_amount = len(room_messages) // 10 if len(room_messages) % 10 == 0 else len(room_messages) // 10 + 1
    pages_list_amount = [x for x in range(1, pages_amount+1)]

    u_message = SubThemeMessage.objects.get(id=mes)
    
    if request.method == "POST":
        u_message.main_text = request.POST.get('main_text')
        u_message.save()
        return redirect('subtheme', pk=pk, page=page)

    context = {
        'room_messages': messages_per_page,
        'room': room,
        'pages_amount': pages_list_amount,
        'is_update': True,
        'u_message': u_message,
        'current_page': page,
        'pk': pk
    }

    return render(request, 'forum_pages/subTheme.html', context)


def updateMessageSandbox(request, pk):
    u_message = SandboxMessage.objects.get(id=pk)
    messages = SandboxMessage.objects.all().order_by('-id')
    main_banner = MainPictureBanner.objects.all()[0]

    if request.method == "POST":
        u_message.main_text = request.POST.get('main_text')
        u_message.save()
        return redirect('sandbox')

    context = {
        'messages': messages,
        'is_update': True,
        'u_message': u_message,
        'main_banner': main_banner
    }

    return render(request, 'forum_pages/sandbox.html', context)

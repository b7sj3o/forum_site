from django.shortcuts import render, redirect, get_object_or_404
from .models import Advertisements, MainPictureBanner, MainTextBanner, UserData, SubThemeMessage, Themes, SandboxMessage, User, SubThemes, TopAgency
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.db.models import Q
from django.contrib import messages


# -------------- RENDER --------------

# ----------- READ -----------

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

    if not messages_per_page:
        pages_amount = 1
    else:
        pages_amount = len(
            messages) // 10 if len(messages) % 10 == 0 else len(messages) // 10 + 1
    pages_list_amount = list(range(1, pages_amount+1))

    if page > pages_amount and pages_amount:
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
    if not pages_amount:
        pages_amount = 1
    pages_list_amount = list(range(1, pages_amount+1))

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

    any_result = not len(subthemes)

    subthemes_per_page = subthemes[page*10-10:page*10]
    pages_amount = len(
        subthemes) // 10 if len(subthemes) % 10 == 0 else len(subthemes) // 10 + 1
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
        pages_amount = len(
            room_messages) // 10 if len(room_messages) % 10 == 0 else len(room_messages) // 10 + 1

    pages_list_amount = list(range(1, pages_amount+1))
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


def userProfile(request, pk):
    user = User.objects.get(username=pk)
    cuser = user
    themes_amount = len(SubThemes.objects.filter(user=user))

    last_themes = SubThemeMessage.objects.filter(
        user=user).order_by('-created')[:10]
    messages_amount = len(last_themes)

    user_forms = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.username)

    context = {
        'cuser': cuser,
        'themes_amount': themes_amount,
        'messages_amount': messages_amount,
        'user_forms': user_forms,
        'last_themes': last_themes,
    }
    return render(request, 'forum_pages/user-profile.html', context)


def search(request):
    q = request.GET.get('q')
    if not q:
        return redirect(request.META.get('HTTP_REFERER', None))
    return redirect('searched-subthemes', page=1, q=q)


def agencyPage(request):
    agencies = TopAgency.objects.all().order_by('-id')
    context = {
        'agencies': agencies
    }
    return render(request, 'forum_pages/agency.html', context)


def advertPage(request):
    context = {}
    return render(request, 'forum_pages/advertisment.html', context)


def adminPanel(request):

    context = {}
    return render(request, 'forum_pages/admin-panel.html', context)

def policy(request):
    return render(request, 'forum_pages/policy.html')

def advertisementPage(request, pk, adv_type):
    advert = None
    print(pk)
    try:
        if adv_type == 'first_advertisment':
            advert = MainTextBanner.objects.get(id=pk)
        elif adv_type == 'second_advertisment':
            advert = MainPictureBanner.objects.get(id=pk)
        elif adv_type == 'third_advertisment':
            advert = TopAgency.objects.get(id=pk)
    except:
        ...

    context = {
        'advert': advert # TITLE, IMAGE, DETAILED_TEXT, LINK
    }
    return render(request, 'forum_pages/advertisment_page.html', context)
# -------- CREATE --------


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
    return render(request, 'forum_pages/create-subtheme.html', context)


def createAgency(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.filter(username=username).first()

        if not user:
            messages.success(request, ('Користувача з таким іменем не існує'))
            return redirect('create-agency')

        TopAgency.objects.create(
            user=user,
            title=request.POST.get('title'),
            name=request.POST.get('name'),
            banner=request.FILES.get('banner')
        )
        return redirect('agency')

    context = {}
    return render(request, 'forum_pages/create-agency.html', context)


def createTheme(request):
    if request.POST:
        Themes.objects.create(
            title=request.POST.get('title')
        )
        return redirect('all-themes')
    return render(request, 'forum_pages/create-theme.html')


def createMessageAdvert(request):
    if request.POST:
        MainTextBanner.objects.all().delete()

        MainTextBanner.objects.create(
            title=request.POST.get('title'),
            text=request.POST.get('text')
        )
        return redirect('home')
    return render(request, 'forum_pages/create-message-advert.html')


def createBanner(request):
    if request.POST:
        MainPictureBanner.objects.all().delete()

        MainPictureBanner.objects.create(
            image=request.FILES.get('image')
        )
        return redirect('home')
    return render(request, 'forum_pages/create-banner.html')

# -------- UPDATE --------


def updateMessage(request, pk, mes, page):
    room = SubThemes.objects.get(id=pk)
    room_messages = room.subtheme_messages.all().order_by('-id')

    messages_per_page = room_messages[page*10-10:page*10]
    pages_amount = len(
        room_messages) // 10 if len(room_messages) % 10 == 0 else len(room_messages) // 10 + 1
    pages_list_amount = list(range(1, pages_amount+1))

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


def updateMessageSandbox(request, pk, page):
    messages = SandboxMessage.objects.all().order_by('-created')
    messages_per_page = messages[page*10-10:page*10]

    pages_amount = len(
        messages) // 10 if len(messages) % 10 == 0 else len(messages) // 10 + 1
    pages_list_amount = list(range(1, pages_amount+1))

    u_message = SandboxMessage.objects.get(id=pk)
    main_banner = MainPictureBanner.objects.all()[0]

    if request.method == "POST":
        u_message.main_text = request.POST.get('main_text')
        u_message.save()
        return redirect('sandbox', page=page)

    context = {
        'messages': messages_per_page,
        'pages_amount': pages_list_amount,
        'current_page': page,
        'is_update': True,
        'u_message': u_message,
        'main_banner': main_banner,
    }

    return render(request, 'forum_pages/sandbox.html', context)


# -------- DELETE --------

def deleteSubTheme(request, pk):
    referer = request.META.get('HTTP_REFERER', None)

    subtheme = SubThemes.objects.get(id=pk)
    subtheme.delete()

    return redirect(referer)


def deleteMessage(request, pk):
    referer = request.META.get('HTTP_REFERER', None)
    if 'sandbox' in referer:
        message = SandboxMessage.objects.get(id=pk)
    else:
        message = SubThemeMessage.objects.get(id=pk)
    message.delete()

    return redirect(referer)


def deleteTheme(request, pk):
    referer = request.META.get('HTTP_REFERER', None)

    theme = Themes.objects.get(id=pk)
    theme.delete()

    return redirect(referer)

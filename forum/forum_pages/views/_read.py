from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from ..models import (Advertisement,
                      MainPictureBanner,
                      MainTextBanner,
                      SubThemeMessage,
                      Theme,
                      SandboxMessage,
                      User,
                      SubTheme,
                      TopAgency,
                      BaseTheme,
                      AgencyJobOrganization
                      )
from ..forms import (
    UserForm,
    BaseThemeForm
    )


def index(request):
    advertisements = Advertisement.objects.all().order_by('-id')
    themes = Theme.objects.all().order_by('-id')
    agencies = AgencyJobOrganization.objects.all().order_by('-id')

    chosen_product = MainTextBanner.objects.last()
    main_banner = MainPictureBanner.objects.last()

    last_messages = SandboxMessage.objects.all().order_by('-id')[:5]

    context = {
        'advertisements': advertisements,
        'chosen_product': chosen_product,
        'main_banner': main_banner,
        'last_messages': last_messages,
        'themes': themes,
        'agencies': agencies,
    }

    return render(request, 'index.html', context=context)


def sandbox(request):
    main_banner = MainPictureBanner.objects.all()[0]
    messages = SandboxMessage.objects.all().order_by('-updated')

    # set up Pagination
    p = Paginator(messages, 10)
    page = request.GET.get('page')
    paginator = p.get_page(page)

    # form to create message in sandbox
    if request.method == 'POST':
        message = SandboxMessage.objects.create(
            user=request.user,
            main_text=request.POST.get('main_text')
        )
        return redirect('sandbox')

    context = {
        'main_banner': main_banner,
        'paginator': paginator
    }

    return render(request, 'sandbox.html', context)


def allThemes(request):
    themes = Theme.objects.all().order_by('-id')

    context = {
        'themes': themes
    }
    return render(request, 'allThemes.html', context)


def subThemes(request, pk):
    theme = Theme.objects.get(id=pk)
    subthemes = theme.subthemes.all().order_by('-created')

    # set up Pagination
    p = Paginator(subthemes, 10)
    page = request.GET.get('page')
    paginator = p.get_page(page)

    context = {
        'theme': theme,
        'paginator': paginator
    }
    return render(request, 'subThemes.html', context)


def searchedSubThemes(request):
    q = request.GET.get('q')
    keywords = q.split()

    # filter subthemes
    query = Q()
    for keyword in keywords:
        query |= Q(title__icontains=keyword) | Q(main_text__icontains=keyword)
    subthemes = SubTheme.objects.filter(query).order_by('-created')
    # set up Pagination
    p = Paginator(subthemes, 10)
    page = request.GET.get('page')
    paginator = p.get_page(page)


    context = {
        'paginator': paginator,
        'content_amount': p.count,
        'requested_words': q
    }

    return render(request, 'searched-subthemes.html', context)


def subTheme(request, pk):
    subtheme = SubTheme.objects.get(id=pk)
    subtheme_messages = subtheme.subtheme_messages.all().order_by('-id')

    # set up Pagination
    p = Paginator(subtheme_messages, 10)
    page = request.GET.get('page')
    paginator = p.get_page(page)

    if request.method == 'POST':
        theme = SubThemeMessage.objects.create(
            user=request.user,
            subtheme=subtheme,
            main_text=request.POST.get('main_text')
        )
        subtheme.count += 1
        subtheme.save()
        return redirect('subtheme', pk=pk)

    context = {
        'paginator': paginator,
        'subtheme': subtheme
    }
    return render(request, 'subTheme.html', context)


def userProfile(request, pk):
    user = User.objects.get(username=pk)

    themes_amount = len(SubTheme.objects.filter(user=user))
    messages_by_user = SubThemeMessage.objects.filter(
        user=user).order_by('-created')
    messages_amount = len(messages_by_user)
    last_themes = messages_by_user[:10]

    user_forms = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            messages.success(
                request, ('Ви успішно змінили дані свого профілю!'))
        else:
            messages.success(request, ('Цей нікнейм/E-mail вже зайнятий'))

        return redirect('user-profile', pk=user.username)

    context = {
        'cuser': user,
        'themes_amount': themes_amount,
        'messages_amount': messages_amount,
        'user_forms': user_forms,
        'last_themes': last_themes,
    }
    return render(request, 'user-profile.html', context)


def agencyPage(request):
    agencies = TopAgency.objects.all().order_by('-id')
    context = {
        'agencies': agencies
    }
    return render(request, 'top-agency.html', context)


def advertPage(request):
    context = {}
    return render(request, 'advertisment.html', context)


def adminPanel(request):
    if request.user.username != 'admin':
        return redirect('home')
    context = {}
    return render(request, 'admin-panel.html', context)


def policy(request):
    return render(request, 'policy.html')


def advertisementPage(request, pk, adv_type):
    advert = None
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
        'advert': advert  # TITLE, IMAGE, DETAILED_TEXT, LINK
    }
    return render(request, 'advertisment_page.html', context)


def specific_theme_page(request, assoc):
    if request.user.username != 'admin':
        return redirect('home')

    form = BaseThemeForm()
    themes = BaseTheme.objects.filter(assoc=assoc)

    context = {
        'themes': themes,
        'form': form,
        'assoc': assoc
    }
    return render(request, 'specific_theme_page.html', context)

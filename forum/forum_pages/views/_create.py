from django.contrib import messages
from django.shortcuts import render, redirect


from ..models import (
    MainTextBanner,
    User,
    TopAgency,
    Theme,
    SubTheme,
)
from ..forms import (
    MainPictureBannerForm,
    MainTextBannerForm,
    AdvertismentForm,
    ThemeForm,
    TopAgencyForm,
    SubThemeForm,
    BaseThemeForm,
    AgencyJobOrganizationForm
)


def createAdvertisment(request):
    form = AdvertismentForm()
    if request.method == "POST":
        _form = AdvertismentForm(request.POST)
        if _form.is_valid():
            adv = _form.save(commit=False)
            adv.name = request.user
            adv.save()
            return redirect('home')
        return redirect('create-advertisment')
    context = {
        'form': form
    }
    return render(request, 'create-advertisment.html', context)


def createSubTheme(request, topic_id):
    base_theme = Theme.objects.get(pk=topic_id)
    form = SubThemeForm()

    if request.method == "POST":
        _form = SubThemeForm(request.POST)
        if _form.is_valid():
            subtheme = _form.save(commit=False)
            subtheme.user = request.user
            subtheme.base_theme = base_theme
            subtheme.save()

        return redirect('subthemes', pk=topic_id)

    context = {
        'form': form
    }

    return render(request, 'create-subtheme.html', context)


def createAgency(request):
    form = TopAgencyForm()
    if request.method == 'POST':
        _form = TopAgencyForm(request.POST, request.FILES)
        if _form.is_valid():
            _form.save()

        return redirect('agency')

    context = {
        'form': form
    }
    return render(request, 'create-top-agency.html', context)


def createTheme(request):
    form = ThemeForm()
    if request.POST:
        _form = ThemeForm(request.POST)
        if _form.is_valid():
            _form.save()

        return redirect('create-theme')

    context = {
        'form': form
    }
    return render(request, 'create-theme.html', context)


def createMessageAdvert(request):
    form = MainTextBannerForm()
    if request.POST:
        _form = MainTextBannerForm(request.POST, request.FILES)
        if _form.is_valid():
            banner_item = MainTextBanner.objects.first()
            if banner_item:
                banner_item.delete()

            _form.save()
            return redirect('home')

        return redirect('create-message-advert')

    context = {
        'form': form
    }
    return render(request, 'create-message-advert.html', context)


def createBanner(request):
    form = MainPictureBannerForm()

    if request.method == 'POST':
        _form = MainPictureBannerForm(request.POST, request.FILES)

        if _form.is_valid():
            _form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'create-banner.html', context)


def createSpecificTheme(request, assoc):

    if request.method == 'POST':
        form = BaseThemeForm(request.POST)

        if form.is_valid():
            theme = form.save(commit=False)
            theme.user = request.user
            theme.assoc = assoc

            theme.save()

            return redirect('specific_theme_page', assoc=assoc)

    return render(request, 'specific_theme_page.html')

def createAgencyJobOrganization(request):
    form = AgencyJobOrganizationForm()

    if request.method == "POST":
        _form = AgencyJobOrganizationForm(request.POST)

        if _form.is_valid():
            _form.save()

            return redirect('create-agency-job-org')

    context = {
        'form': form
    }

    return render(request, 'create-agency-job-org.html', context)
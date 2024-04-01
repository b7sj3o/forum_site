from django.shortcuts import render, redirect
from django.core.paginator import Paginator


from ..models import (
    MainPictureBanner,
    SubThemeMessage,
    SandboxMessage,
    SubTheme,
)


def updateMessage(request, pk, mes):
    subtheme = SubTheme.objects.get(id=pk)
    subtheme_messages = subtheme.subtheme_messages.all().order_by('-id')

    # set up Pagination
    p = Paginator(subtheme_messages, 10)
    page = request.GET.get('page')
    paginator = p.get_page(page)

    u_message = SubThemeMessage.objects.get(id=mes)

    if request.method == "POST":
        u_message.main_text = request.POST.get('main_text')
        u_message.save()
        return redirect('subtheme', pk=pk)

    context = {
        'paginator': paginator,
        'is_update': True,
        'u_message': u_message,
        'subtheme': subtheme
    }

    return render(request, 'subTheme.html', context)


def updateMessageSandbox(request, pk):
    sandbox_messages = SandboxMessage.objects.all().order_by('-id')

    # set up Pagination
    p = Paginator(sandbox_messages, 10)
    page = request.GET.get('page')
    paginator = p.get_page(page)

    u_message = SandboxMessage.objects.get(id=pk)
    main_banner = MainPictureBanner.objects.all()[0]

    if request.method == "POST":
        u_message.main_text = request.POST.get('main_text')
        u_message.save()
        return redirect('sandbox')

    context = {
        'paginator': paginator,
        'is_update': True,
        'u_message': u_message,
        'main_banner': main_banner
    }

    return render(request, 'sandbox.html', context)

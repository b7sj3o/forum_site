from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView

from typing import Any
import json

from ..models import (SubThemeMessage,
                      Theme,
                      SandboxMessage,
                      User,
                      SubTheme,
                      AgencyJobOrganization
                      )


class SearchUserList(ListView):
    model = User
    template_name = 'ban-user.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(list(User.objects.values('username')))
        return context


def deleteSubTheme(request, pk):
    referer = request.META.get('HTTP_REFERER', None)

    subtheme = SubTheme.objects.get(id=pk)
    subtheme.delete()

    return redirect(referer)


def deleteMessage(request, pk, subtheme_id):
    referer = request.META.get('HTTP_REFERER', None)
    if 'sandbox' in referer:
        message = SandboxMessage.objects.get(id=pk)
    else:
        message = SubThemeMessage.objects.get(id=pk)
        subtheme = SubTheme.objects.get(id=subtheme_id)
        subtheme.count -= 1
        subtheme.save()
    message.delete()

    return redirect(referer)


def deleteTheme(request, pk):
    referer = request.META.get('HTTP_REFERER', None)

    theme = Theme.objects.get(id=pk)
    theme.delete()

    return redirect(referer)


def banUser(request):
    if request.user != 'admin':
        return redirect('home')

    if request.POST:
        username = request.POST.get('username')
        ban_reason = request.POST.get('main_text')

        user = User.objects.get(username=username)

        if user == request.user or user.username == 'admin':
            messages.success(request, 'Ви не можете заблокувати свій профіль!')
            return redirect('ban-user-page')

        user.is_blocked = True
        user.ban_reason = ban_reason
        user.save()

        messages.success(request, "Користувача успішно заблоковано")

    return redirect('ban-user')

def deleteAgencyJobOrg(request, pk):
    referer = request.META.get('HTTP_REFERER', None)
    agency = get_object_or_404(AgencyJobOrganization, id=pk)
    
    if agency: agency.delete()

    return redirect(referer)
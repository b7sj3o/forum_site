import json
from django.http import HttpResponseForbidden
from django.shortcuts import render
from forum_members.views import logout_user


class CheckUserAccess:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if 'logout' in str(request):
            return logout_user(request)
        elif 'img' in str(request):
            return response

        if request.user.is_authenticated:
            if request.user.is_blocked:
                return render(request, 'blocked-page.html')

        return response

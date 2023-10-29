from django.shortcuts import render


def index(request):
    return render(request, 'forum_pages/base.html')



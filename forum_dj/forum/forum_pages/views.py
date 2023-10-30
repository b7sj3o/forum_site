from django.shortcuts import render


def index(request):
    return render(request, 'forum_pages/base.html')

def sass_page_handler(request):
    return render(request, 'forum_pages/base.html')
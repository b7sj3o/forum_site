from django.shortcuts import render
from .models import Advertisements

def index(request):
    data = Advertisements.objects.all()
    return render(request, 'forum_pages/index.html', {'data': data})

# def sass_page_handler(request):
#     return render(request, 'forum_pages/index.html')
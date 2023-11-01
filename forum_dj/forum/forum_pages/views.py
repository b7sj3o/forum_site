from django.shortcuts import render, redirect
from .models import Advertisements, MainBanner, ChosenProduct, UserData
import random

# -------------- RENDER -------------- 

def index(request):
    advertisements = Advertisements.objects.all().order_by('-time')
    chosen_product = ChosenProduct.objects.get()
    main_banners = MainBanner.objects.all()
    main_banner = random.choice(main_banners)

    sandbox = UserData.objects.all().order_by('-id')[:5]

    return render(request, 'forum_pages/index.html',{
        'advertisements': advertisements,
        'chosen_product': chosen_product,
        'main_banner': main_banner,
        'sandbox': sandbox
    })

def sandbox(request):
    users = UserData.objects.all()
    return render(request, 'forum_pages/sandbox.html', {'users': users})

def signup(request):
    return render(request, '')

def login(request):
    pass

# -------------- NOT RENDER -------------- 

def save_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        main_text = request.POST.get('main_text')
        
        existing_user = UserData.objects.filter(name=name, main_text=main_text).first()
        if not existing_user:
            UserData.objects.create(name=name, main_text=main_text)
        
        users = UserData.objects.all()
        return render(request, 'forum_pages/sandbox.html', {'users': users})
    
def clear_data(request):
    UserData.objects.all().delete()
    return render(request, 'forum_pages/sandbox.html', {'users': None})
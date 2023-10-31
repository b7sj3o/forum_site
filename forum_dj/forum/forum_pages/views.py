from django.shortcuts import render
from .models import Advertisements, MainBanner, ChosenProduct
import random

def index(request):
    advertisements = Advertisements.objects.all()
    chosen_product = ChosenProduct.objects.get()
    main_banners = MainBanner.objects.all()
    main_banner = random.choice(main_banners)

    return render(request, 'forum_pages/index.html',{
        'advertisements': advertisements,
        'chosen_product': chosen_product,
        'main_banner': main_banner
    })



# def sass_page_handler(request):
#     return render(request, 'forum_pages/index.html')
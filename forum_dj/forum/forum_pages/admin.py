from django.contrib import admin
from .models import Advertisements, ChosenProduct, MainBanner, Message

admin.site.register(Advertisements)
admin.site.register(ChosenProduct)
admin.site.register(MainBanner)
admin.site.register(Message)
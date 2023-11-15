from django.contrib import admin
from .models import Advertisements, MainPictureBanner, MainTextBanner, ThemeMessage, Themes

admin.site.register(Advertisements)
admin.site.register(MainTextBanner)
admin.site.register(MainPictureBanner)
admin.site.register(ThemeMessage)
admin.site.register(Themes)
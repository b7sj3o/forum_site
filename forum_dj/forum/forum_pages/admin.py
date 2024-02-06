from django.contrib import admin
from .models import Advertisements, MainPictureBanner, MainTextBanner, SubThemeMessage, Themes, User, SubThemes, TopAgency, BaseTheme

admin.site.register(Advertisements)
admin.site.register(MainTextBanner)
admin.site.register(MainPictureBanner)
admin.site.register(SubThemeMessage)
admin.site.register(Themes)
admin.site.register(SubThemes)
admin.site.register(User)
admin.site.register(TopAgency)
admin.site.register(BaseTheme)

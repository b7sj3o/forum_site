from django.contrib import admin
from .models import (
    Advertisement,
    MainPictureBanner, 
    MainTextBanner, 
    SubThemeMessage, 
    Theme, 
    User, 
    SubTheme, 
    TopAgency, 
    BaseTheme, 
    SandboxMessage,
    AgencyJobOrganization
)

admin.site.register(Advertisement)
admin.site.register(MainTextBanner)
admin.site.register(MainPictureBanner)
admin.site.register(SubThemeMessage)
admin.site.register(Theme)
admin.site.register(SubTheme)
admin.site.register(User)
admin.site.register(TopAgency)
admin.site.register(BaseTheme)
admin.site.register(SandboxMessage)
admin.site.register(AgencyJobOrganization)

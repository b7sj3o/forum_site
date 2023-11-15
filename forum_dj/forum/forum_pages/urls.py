from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sandbox', views.sandbox, name='sandbox'),
    path('themes', views.themes, name='themes'),
    path('theme<str:pk>', views.theme, name='theme'),

    path('delete-message<str:pk>', views.deleteMessage, name='delete-message'),
    path('delete-theme<str:pk>', views.deleteTheme, name='delete-theme'),
]

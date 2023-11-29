from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sandbox', views.sandbox, name='sandbox'),
    path('themes', views.themes, name='themes'),
    path('theme/<str:user>/<str:pk>/', views.theme, name='theme'),

    path('create-theme', views.createTheme, name='create-theme'),
    path('create-advertisment', views.createAdvertisment, name='create-advertisment'),


    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('delete-theme/<str:pk>/', views.deleteTheme, name='delete-theme'),

    path('user-profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('search', views.search, name='search'),

]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sandbox', views.sandbox, name='sandbox'),
    path('all-themes', views.allThemes, name='all-themes'),
    path('subthemes/<str:pk>', views.subThemes, name='subthemes'),
    path('subtheme/<str:user>/<str:pk>/', views.subTheme, name='subtheme'),
    path('advert-page', views.advertPage, name='advert-page'),

    path('create-subtheme/<str:topic_id>', views.createSubTheme, name='create-subtheme'),
    path('create-advertisment', views.createAdvertisment, name='create-advertisment'),

    path('update-message/<str:pk>/<str:pk2>/', views.updateMessage, name='update-message'),
    path('update-message-sandbox/<str:pk>/', views.updateMessageSandbox, name='update-message-sandbox'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('delete-subtheme/<str:pk>/', views.deleteSubTheme, name='delete-subtheme'),

    path('user-profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('search', views.search, name='search'),

]

from django.urls import path
from . import views
from . import middleware

urlpatterns = [
    # ------------ READ ------------
    path('', views.index, name='home'),
    path('sandbox&page=<int:page>', views.sandbox, name='sandbox'),
    path('all-themes', views.allThemes, name='all-themes'),
    path('subthemes/&subthemeId=<str:pk>&page=<int:page>', views.subThemes, name='subthemes'),
    path('searched-subthemes/&page=<int:page>/&q=<str:q>', views.SearchedsubThemes, name='searched-subthemes'),
    path('subtheme&subthemeId=<str:pk>&page=<int:page>', views.subTheme, name='subtheme'),
    path('advert-page', views.advertPage, name='advert-page'),
    path('agency', views.agencyPage, name='agency'),
    path('policy', views.policy, name='policy'),
    path('advertisement-page/<str:pk>/<str:adv_type>', views.advertisementPage, name='advertisement-page'),
    path('blocked-page', middleware.CheckUserAccess, name='blocked-page'),
    path('search', views.search, name='search'),
    path('admin-panel', views.adminPanel, name='admin-panel'),
    path('user-profile/<str:pk>/', views.userProfile, name='user-profile'),

    # ------------ CREATE ------------
    path('create-theme', views.createTheme, name='create-theme'),
    path('create-subtheme/<str:topic_id>', views.createSubTheme, name='create-subtheme'),
    path('create-advertisment', views.createAdvertisment, name='create-advertisment'),
    path('create-agency', views.createAgency, name='create-agency'),
    path('create-message-advert', views.createMessageAdvert, name='create-message-advert'),
    path('create-banner', views.createBanner, name='create-banner'),

    # ------------ UPDATE ------------
    path('update-message/&subthemeId=<str:pk>&messageId<str:mes>&page=<int:page>', views.updateMessage, name='update-message'),
    path('update-message-sandbox&messageId=<str:pk>&page=<int:page>', views.updateMessageSandbox, name='update-message-sandbox'),

    # ------------ DELETE ------------
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('delete-theme/<str:pk>/', views.deleteTheme, name='delete-theme'),
    path('delete-subtheme/<str:pk>/', views.deleteSubTheme, name='delete-subtheme'),
    path('ban-user', views.banUser, name='ban-user'),




]

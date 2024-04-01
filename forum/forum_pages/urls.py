from django.urls import path
from . import views
from . import middleware

urlpatterns = [
    # ------------ READ ------------
    path('', views.index, name='home'),
    path('sandbox', views.sandbox, name='sandbox'),
    path('all-themes', views.allThemes, name='all-themes'),
    path('subthemes/<str:pk>', views.subThemes, name='subthemes'),
    path('searched-subthemes', views.searchedSubThemes, name='searched-subthemes'),
    path('subtheme/<str:pk>', views.subTheme, name='subtheme'),
    path('advert-page', views.advertPage, name='advert-page'),
    path('agency', views.agencyPage, name='agency'),
    path('policy', views.policy, name='policy'),
    path('advertisement-page/<str:pk>/<str:adv_type>', views.advertisementPage, name='advertisement-page'),
    path('blocked-page', middleware.CheckUserAccess, name='blocked-page'),
    path('admin-panel', views.adminPanel, name='admin-panel'),
    path('user-profile/<str:pk>/', views.userProfile, name='user-profile'),
    path('specific_theme_page/<str:assoc>/', views.specific_theme_page, name='specific_theme_page'),

    # ------------ CREATE ------------
    path('create-theme', views.createTheme, name='create-theme'),
    path('create-subtheme/<str:topic_id>', views.createSubTheme, name='create-subtheme'),
    path('create-advertisment', views.createAdvertisment, name='create-advertisment'),
    path('create-agency', views.createAgency, name='create-agency'),
    path('create-message-advert', views.createMessageAdvert, name='create-message-advert'),
    path('create-banner', views.createBanner, name='create-banner'),
    path('create-specific-theme<str:assoc>', views.createSpecificTheme, name='create-specific-theme'),
    path('create-agency-job-org', views.createAgencyJobOrganization, name='create-agency-job-org'),

    # ------------ UPDATE ------------
    path('update-message/<str:pk>/<str:mes>/', views.updateMessage, name='update-message'),
    path('update-message-sandbox/<str:pk>/', views.updateMessageSandbox, name='update-message-sandbox'),

    # ------------ DELETE ------------
    path('delete-message/<str:pk>/<int:subtheme_id>/', views.deleteMessage, name='delete-message'),
    path('delete-theme/<str:pk>/', views.deleteTheme, name='delete-theme'),
    path('delete-subtheme/<str:pk>/', views.deleteSubTheme, name='delete-subtheme'),
    path('ban-user', views.banUser, name='ban-user'),
    path('delete-agency-job-org/<int:pk>', views.deleteAgencyJobOrg, name='delete-agency-job-org')




]

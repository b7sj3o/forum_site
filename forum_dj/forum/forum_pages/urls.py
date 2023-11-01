from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sandbox', views.sandbox, name='sandbox'),

    path('save_data/', views.save_data, name='save_data'),
    path('clear_data/', views.clear_data, name='clear_data'),      
]

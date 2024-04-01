from django.contrib import admin
from django.urls import path, include
from forum_pages import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ban-user-page', views.SearchUserList.as_view(), name='ban-user-page'),
    path('', include('forum_pages.urls')),
    path('forum_members/', include('django.contrib.auth.urls')),
    path('forum_members/', include('forum_members.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


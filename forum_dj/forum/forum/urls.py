from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from forum_pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('forum_pages.urls')),
    path('forum_members/', include('django.contrib.auth.urls')),
    path('forum_members/', include('forum_members.urls'))
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
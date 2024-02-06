from django.contrib import admin
from django.urls import path, include
from forum_pages import views
from django.conf import settings
from django.conf.urls.static import static
from .settings import STATIC_ROOT, STATIC_URL, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-search', views.SearchUserList.as_view(), name='user-search'),
    path('', include('forum_pages.urls')),
    path('forum_members/', include('django.contrib.auth.urls')),
    path('forum_members/', include('forum_members.urls')),
]


urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

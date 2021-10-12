from django.contrib import admin
from django.urls import path, include

from personal.views import (
    home_screen_view,
)

from account.views import (
    register_view,
    login_view,
    logout_view,
)

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('admin/', admin.site.urls),
    path('', include('Dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
=======
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
>>>>>>> ac0158286850c6fce9e2514e0e816d2cc6819814

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
<<<<<<< HEAD
    path('', include('Dashboard.urls')),
=======
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
>>>>>>> ac0158286850c6fce9e2514e0e816d2cc6819814
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

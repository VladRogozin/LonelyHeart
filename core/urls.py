from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from cat.views import cat_base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cat_base, name='cat_base'),
    path('cat/', include('cat.urls')),
    path('game/', include('game.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
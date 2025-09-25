from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),  # til almashtirish uchun
]

# Default til EN bo‘ladi
urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
)

# Media va static fayllar doim til prefiksiz bo‘lishi kerak
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

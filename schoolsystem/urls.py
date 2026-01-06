"""schoolsystem URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Main website (Core app)
    path("", include("core.urls")),
    
    # Admin Panel
    path('admin/', admin.site.urls),
    
    # API IS REMOVED HERE
    # path("api/", include("api.urls")), 
]

# Serve media files in development (images, etc.)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
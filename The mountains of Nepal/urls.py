from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('sssr_mounts/', include('sssr_mounts.urls')),
    path('russian_mounts/', include('russian_mounts.urls')),
    path('nepal_mounts/', include('nepal_mounts.urls')),
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
]

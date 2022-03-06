from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('site/', include('maps_site.urls')),
    path('api/', include('maps_api.urls')),
    path('admin/', admin.site.urls),
]

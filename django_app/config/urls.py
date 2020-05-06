from django.contrib import admin
from django.urls import path, include

from apps.api.urls import urls as api_urls


urlpatterns = [
    path('api/v1/', include(api_urls)),
    path('admin/', admin.site.urls),
]

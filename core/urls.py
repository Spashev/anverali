from django.contrib import admin
from django.urls import path, include

from core.swagger import swagger_patterns

urlpatterns = [
    path('swagger/', include(swagger_patterns)),
    path('admin/', admin.site.urls),
    path('api/v1/', include('webhook.urls'))
]

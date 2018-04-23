
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/simple_rest', include("simple_rest.api.urls", namespace="rest")),
]

from django.contrib import admin
from django.urls import include, path

BASE_URL = 'api/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_URL, include('apps.user.router'))
]

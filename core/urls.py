from django.contrib import admin
from django.urls import include, path

BASE_URL = 'api/'

urlpatterns = [
    path(route='admin/', view=admin.site.urls),
    path(route=BASE_URL, view=include('apps.note.router')),
    path(route=BASE_URL, view=include('apps.user.router')),
]

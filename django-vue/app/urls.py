
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('home.urls') )
]


from django import urls, views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('blogSite/', include('blogSite.urls')),
    path('sobre/', include('sobre.urls')),
    
]

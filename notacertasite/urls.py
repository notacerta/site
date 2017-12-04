"""
notacertasite URL Configuration
"""
from django.urls import path, include
from django.contrib import admin
from notacertablog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notacertablog.urls'))
]
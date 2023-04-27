from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # add url for homepage
    path('', views.index, name='homepage'),
]
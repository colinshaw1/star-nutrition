from django.urls import path
from . import views

urlpatterns = [
    # url to the check out funciton
    path('', views.checkout, name='checkout')
]
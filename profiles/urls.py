from django.urls import path
from . import views

urlpatterns = [
    # url to link the proile view
    path('', views.profile, name='profile')
]
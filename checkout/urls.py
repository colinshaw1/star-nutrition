from django.urls import path
from . import views

urlpatterns = [
    # url to the check out funciton
    path('', views.checkout, name='checkout'),
    path('checkout_sucess/<order_number>', views.checkout_success, name='checkout_success'),
]
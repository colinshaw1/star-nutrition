from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    # url to the check out funciton
    path('', views.checkout, name='checkout'),
    # checkout success url
    path('checkout_sucess/<order_number>', views.checkout_success, name='checkout_success'),
    # checkout data url
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    # webhook url
    path('wh/', webhook, name='webhook'),
]
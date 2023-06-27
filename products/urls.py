from django.urls import path
from . import views

# view to call products   
urlpatterns = [
    path('', views.products_view, name='products')
]
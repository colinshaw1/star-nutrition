from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # # adding alluath urls to project level file
    # path('accounts', include('allauth.urls')),
]

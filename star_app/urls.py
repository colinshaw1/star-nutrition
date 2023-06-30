from django.contrib import admin
from django.urls import path
from django.urls import path, include
# add imports for static files
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # # adding alluath urls to project level file
    # path('accounts', include('allauth.urls')),
    #adding homepage urls to project level file
    path('', include('homepage.urls')),
    # adding products urls to project level file
    path('products/', include('products.urls')),
    # adding shoppingbag urls to project level file
    path('shoppingbag/', include('bag.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#using static function to add url to media urls

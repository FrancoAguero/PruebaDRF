
from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from Apps.shop import views
from django.conf import settings
from django.conf.urls.static import static


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    #admin URLS
    path('admin/', admin.site.urls),

    #Local URLS
    path('shop/', include(('Apps.shop.urls', 'Apps.shop'),  namespace='shop')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
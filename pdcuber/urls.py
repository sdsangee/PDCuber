from django.conf.urls import include, url
from django.contrib import admin
#Copied from django documents to serve static files during developement 
#https://docs.djangoproject.com/en/1.9/howto/static-files/

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'pdcuber.views.home', name='home'),
    url(r'', include('pdblogapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'pdcuber.views.home', name='home'),
    url(r'', include('pdblogapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

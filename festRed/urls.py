from django.conf.urls import patterns, include, url
from django.contrib import admin
from festRedapp.api import DocumentResource


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'festRed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^api/', include(DocumentResource().urls)),
    url(r'^admin/', include(admin.site.urls)),
)

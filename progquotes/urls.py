from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'index.html'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

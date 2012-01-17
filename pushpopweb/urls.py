from django.conf.urls.defaults import patterns, include, url

# Admin functionality
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pushpopweb.views.home', name='home'),
    # url(r'^pushpopweb/', include('pushpopweb.foo.urls')),

    # Admin Page
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

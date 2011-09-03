from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'paullzn.views.home', name='home'),
    # url(r'^paullzn/', include('paullzn.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/greeting/',}),
    (r'^greeting/', include('guestbook.urls')),
    url(r'^api/authenticate/', include('api.authenticate.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^auth/', include('auth1.urls')),
    url(r'^jp/', include('jp.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    
    #('^$', 'django.views.generic.simple.direct_to_template',{'template': 'home.html'}),
    
    (r'^$', 'django.views.generic.simple.redirect_to', {'url': '/greeting/',}),
    (r'^greeting/', include('guestbook.urls')),
	(r'^blog/', include('blog.urls')),
	(r'^auth/', include('auth.urls')),
    # auth specific urls
    #(r'^accounts/create_user/$', 'guestbook.views.create_new_user'),
)

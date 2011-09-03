from django.conf.urls.defaults import *

urlpatterns = patterns('auth1.views',
	(r'^login$',	'login'),
	(r'^login_do$', 'login_do'),
	(r'^logout$', 'logout'),
	(r'^register$', 'register'),
	(r'^register_do$', 'register_do'),
)

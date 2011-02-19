from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
	(r'^$', 'index'),
	(r'^status_up$', 'status_up'),
 	(r'^post$', 'create'),
	(r'^edit$', 'edit'),
	(r'^delete', 'delete')
)

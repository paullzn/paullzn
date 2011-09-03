from django.conf.urls.defaults import *

urlpatterns = patterns('api.authenticate.views',
  (r'^login$', 'login'),
  (r'^logout$', 'logout'),
  (r'^check$', 'check'),
  (r'^create_default$', 'create_default'),
)

from django.conf.urls.defaults import *
import os

urlpatterns = patterns('',
    # Example:
    (r'^$', include('sunming.home.urls')),
    (r'^littlebear/', include('sunming.journalclub.urls')),
    (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(__file__) +'/medias'}),
    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),
)

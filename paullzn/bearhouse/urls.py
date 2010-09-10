from django.conf.urls.defaults import *
import os

urlpatterns = patterns('',
    # Example:
    (r'^album/', include('bearhouse.album.urls')),
    (r'^$', include('bearhouse.home.urls')),
    (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(__file__) +'/medias'}),
    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),
)

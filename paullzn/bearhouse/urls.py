from django.conf.urls.defaults import *
import os

urlpatterns = patterns('',
    # Example:
    (r'^$', include('bearhouse.home.urls')),
    (r'^littlebear/', include('bearhouse.littlebear.urls')),
    (r'^lab/', include('bearhouse.lab.urls')),
    (r'^blog/', include('bearhouse.blog.urls')),
    (r'^album/', include('bearhouse.album.urls')),
    (r'^achieve/', include('bearhouse.achieve.urls')),
    (r'^about/', include('bearhouse.about.urls')),
    (r'^api/', include('bearhouse.api.urls')),
    (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.dirname(__file__) +'/medias'}),
    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),
)

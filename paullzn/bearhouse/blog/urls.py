from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    (r'^$', 'bearhouse.blog.views.index'),
    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),
)

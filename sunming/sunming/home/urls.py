from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    (r'^$', 'bearhouse.home.views.index'),

    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),
)

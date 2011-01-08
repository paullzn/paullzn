from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    (r'^$', 'bearhouse.api.views.index'),
    (r'^insert$', 'bearhouse.api.views.insert'),
    (r'^select$', 'bearhouse.api.views.select'),
    # Uncomment this for admin:
    # (r'^admin/', include('django.contrib.admin.urls')),
)

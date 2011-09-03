#Create your views here.
# Corresponding Django view, "django-guestbook/guestbook/views.py"
from django.core.cache import cache
from django.conf import settings
from django.views.generic.simple import direct_to_template
from blog.models import Blog
from lib import dateutil
def show(request):

	try:
		username = request.session['user']
	except KeyError:
		username = 'anonymous'

	return direct_to_template(request, 'jp/index.html',
			{'username': username, 
			'page': 'jp'})


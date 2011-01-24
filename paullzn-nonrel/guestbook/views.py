# Create your views here.
# Corresponding Django view, "django-guestbook/guestbook/views.py"
from django.core.cache import cache
from django.conf import settings
from django.views.generic.simple import direct_to_template
from guestbook.forms import CreateGreetingForm
from guestbook.models import Greeting
from lib import dateutil
def list_greetings(request):
	#greetings = cache.get(MEMCACHE_GREETINGS)
	#if greetings is None:
	greetings = Greeting.objects.all().order_by('-date')[:10]
	#cache.add(MEMCACHE_GREETINGS, greetings)

	try:
		username = request.session['user']
	except KeyError:
		username = 'anonymous'

	displays = []
	for greeting in greetings:
		d = dateutil.date_to_local(greeting.date)
		if username != 'anonymous' or greeting.isprivate == 0:
			displays.append({'author': greeting.author, 'content': greeting.content, 'date': d, 'isprivate': greeting.isprivate})
	return direct_to_template(request, 'guestbook/index.html',
			{'username': username, 
			'greetings': displays,
			'page': 'about'})

from django.http import HttpResponseRedirect

def create_greeting(request):
	if request.method == 'POST':
		greeting = Greeting()
		greeting.content = request.POST.get('content')
		greeting.isprivate = request.POST.get('isprivate')
		if greeting.isprivate == None:
			greeting.isprivate = 0
	try:
		greeting.author = request.session['user']
	except KeyError:
		greeting.author = 'anonymous'
	greeting.save()
	
	cache.delete('greetings')
	return HttpResponseRedirect('/greeting/')
  

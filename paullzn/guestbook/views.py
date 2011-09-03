# Create your views here.
# Corresponding Django view, "django-guestbook/guestbook/views.py"
from django.core.cache import cache
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from guestbook.forms import CreateGreetingForm
from guestbook.models import Greeting
from lib import dateutil
from auth1.models import User

def list_greetings(request):
	greetings = Greeting.objects.all().order_by('-date')[:10]

	try:
		username = request.session['user']
	except KeyError:
		username = 'anonymous'

	displays = []
	for greeting in greetings:
		d = dateutil.date_to_local(greeting.date)

		if username != 'anonymous' or greeting.isprivate == 0:
			displays.append({'author': greeting.author.username,\
					'content': greeting.content,\
					'date': d, \
					'isprivate': greeting.isprivate})

	return direct_to_template(request, 'guestbook/index.html',
			{'username': username,
			'greetings': displays,
			'page': 'about'})


def create_greeting(request):
	if request.method == 'POST':
		greeting = Greeting()
		greeting.content = request.POST.get('content')
		greeting.isprivate = request.POST.get('isprivate')
		if greeting.isprivate == None:
			greeting.isprivate = 0
	
	try:
		user_id = request.session['user_id']
	except KeyError:
		user_id = User.objects.all().filter( username='anonymous')[0].id
	greeting.author = User.objects.get( id = user_id)
	
	greeting.save()
	
	return HttpResponseRedirect('/greeting/')
  

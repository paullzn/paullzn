#Create your views here.
from django.core.cache import cache
from django.conf import settings
from django.views.generic.simple import direct_to_template
from blog.models import Blog, Status
from auth.models import User
from lib import dateutil
def index(request):
	blogs = Blog.objects.all().order_by('-date')
	paullzn = User.objects.all().filter(username = 'paullzn')[0]
	lisa = User.objects.all().filter(username = 'lisa')[0]

	try:
		p_status = Status.objects.all().filter(author = paullzn ).order_by('-created_at')[0].content
	except IndexError:
		p_status = "nothing.."
	try:
		l_status = Status.objects.all().filter(author = lisa ).order_by('-created_at')[0].content
	except IndexError:
		l_status = "nothing.."

	try:
		username = request.session['user']
	except KeyError:
		username = 'anonymous'

	displays = []

	for blog in blogs:
		d = dateutil.date_to_local(blog.date)
		if username != 'anonymous' or blog.isprivate == 0:
			displays.append({'author': blog.author.username, \
					'content': blog.content, \
					'date': d, \
					'isprivate': blog.isprivate, \
					'title': blog.title})

	return direct_to_template(request, 'blog/index.html',
			{'username': username,
			'p_status': p_status,
			'l_status': l_status,
			'blogs': displays,
			'page': 'blog'})

from django.http import HttpResponseRedirect
from auth.models import User

def status_up(request):
	if request.method == 'POST':
		try:
			user_id = request.session['user_id']
		except KeyError:
			return HttpResponseRedirect('/blog/')
		
		status = Status()
		status.author = User.objects.get( id = user_id)
		status.content = request.POST.get('status')
		status.save()
		
	return HttpResponseRedirect('/blog/')

def create(request):
	if request.method == 'POST':
		blog = Blog()
		blog.title = request.POST.get('title')
		blog.content = request.POST.get('content')
		greeting.isprivate = request.POST.get('isprivate')
		if greeting.isprivate == None:
			greeting.isprivate = 0
		greeting.isprivate = request.POST.get('isprivate')
		if greeting.isprivate == None:
			greeting.isprivate = 0
	
	try:
		user_id = request.session['user_id']
		greeting.save()
	except KeyError:
		greeting.author = 'anonymous'
	
	greeting.save()
	
	return HttpResponseRedirect('/greeting/')
  

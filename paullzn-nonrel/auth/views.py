# Create your views here.

from django.core.cache import cache
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from auth.models import User
import logging

def register_do(request):
	password = request.GET.get('password')
	password_repeat = request.GET.get('password_repeat')
	if password != password_repeat:
		return HttpResponseRedirect('/auth/register')
	logging.info( password)
	logging.info( password_repeat)

	user = User()
	user.username = request.GET.get('name')
	user.password = request.GET.get('password')
	user.email = request.GET.get('email')
	user.mobile = request.GET.get('mobile')
	user.save()
	return HttpResponseRedirect('/auth/login')

def register(request):
	return direct_to_template(request, 'auth/register.html', {})

def login(request):
	return direct_to_template(request, 'auth/login.html', {'page' : 'login'})

def login_do(request):
	user = User.objects.all().filter(username=request.GET.get('name')).filter(password=request.GET.get('password'))
	if user:
		request.session['user'] = user[0].username
		request.session['user_id'] = user[0].id
		return HttpResponseRedirect('/greeting/')
	else:
	 	return HttpResponseRedirect('/auth/login')

def logout(request):
	try:
		del request.session['user']
		del request.session['user_id']
	except KeyError:
		pass
	return HttpResponseRedirect('/greeting/')


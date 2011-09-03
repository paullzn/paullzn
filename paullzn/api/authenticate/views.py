#Create your views here.
from django.core.cache import cache
from django.conf import settings
from django.http import HttpResponse
from api.authenticate.models import User, UserToken
import simplejson as json
import sha, time
from Crypto.Cipher import AES 

def create_default(request):
  try:
    user = User.objects.all().filter(username = 'paullzn')[0]
  except IndexError:
    user = User()
    user.username = 'paullzn'
    user.password = '19881010'
    user.type = 'admin'
    user.save()
    return HttpResponse('done')
  return HttpResponse('admin already there!')

def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
      try:
        user = User.objects.all().filter(username = username)[0]
      except IndexError:
        return HttpResponse(json.dumps({'error': True, 'error_msg': 'Can not find the user'})) 
      user_id = user.id
      auth_password = user.password
      if not (str(password) == str(auth_password)):
        return HttpResponse(json.dumps({'error': True, 'error_msg': 'Wrong Password'})) 
      user_token = UserToken()
      user_token.user_id = user_id
      user_token.token = sha.new(username + '\n' + password + '\n' + str(time.time())).hexdigest()
      user_token.save()
      return HttpResponse(json.dumps({'error' : False, 'token' : user_token.token }))
    else:
      return HttpResponse(json.dumps({'error': True, 'error_msg': 'missing username or password'})) 
  return HttpResponse(json.dumps({'error': True, 'error_msg': 'should POST'})) 

def logout(request):
  if request.method == 'POST':
    try:
      user_id = request.POST.get('usertoken')
    except KeyError:
      return HttpResponseRedirect('/blog/')
    
    status = Status()
    status.author = User.objects.get( id = user_id)
    status.content = request.POST.get('status')
    status.save()
    
  return HttpResponse('todo')

def check(request):
  return HttpResponse('false')
  

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
import os

def index(request):
    t = loader.get_template('about/index.html')
    c = Context({'author': 'Paullzn'})
    return HttpResponse(t.render(c), mimetype="text/html")

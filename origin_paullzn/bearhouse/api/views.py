# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
import os

def index(request):
    return HttpResponse("hello world", mimetype="text")

def select(request):
    return "select"

def insert(request):
    return "insert"

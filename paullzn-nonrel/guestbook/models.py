from django.db import models
from auth.models import User
import datetime

class Greeting(models.Model):
	author = models.ForeignKey(User)
	content = models.TextField()
	isprivate = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)

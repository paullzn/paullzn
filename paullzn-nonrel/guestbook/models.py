from django.db import models
from django.contrib.auth.models import User
import datetime

class Greeting(models.Model):
	author = models.CharField(max_length=30)
	content = models.TextField()
	isprivate = models.IntegerField()
	date = models.DateTimeField(auto_now_add=True)
	def getDate(self):
		return datetime.strp(date)

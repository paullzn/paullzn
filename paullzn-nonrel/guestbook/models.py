from django.db import models
from django.contrib.auth.models import User
import datetime

class Greeting(models.Model):
	author = models.CharField(max_length=30)
	content = models.TextField()
	date = models.DateTimeField()
	def getDate(self):
		return datetime.strp(date)

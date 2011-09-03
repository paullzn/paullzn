from django.db import models
from auth1.models import User
import datetime

class Blog(models.Model):
	author = models.ForeignKey(User)
	title = models.TextField()
	content = models.TextField()
	isprivate = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now_add=True)

class Status(models.Model):
	author = models.ForeignKey(User)
	content = models.CharField(max_length=140)
	created_at = models.DateTimeField(auto_now_add=True)

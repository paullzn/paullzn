from django.db import models
import datetime

class User(models.Model):
  username = models.TextField()
  password = models.TextField()
  type = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now_add=True)

class UserToken(models.Model):
  user_id = models.IntegerField()
  token = models.CharField(max_length=140)
  created_at = models.DateTimeField(auto_now_add=True)
  refreshed_at = models.DateTimeField(auto_now_add=True)

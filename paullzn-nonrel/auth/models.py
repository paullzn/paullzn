from django.db import models

class User(models.Model):
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=100)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)

# Create your models here.

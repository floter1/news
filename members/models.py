from django.db import models

# Create your models here.

class Members(models.Model):
	user_name = models.CharField(max_length=250)
	age = models.IntegerField(null=True, blank=True)
	phone = models.CharField(max_length=250)
	upline = models.CharField(max_length=250)
	tin = models.CharField(max_length=250)
	points = models.FloatField(null=True, blank=True)
	money = models.FloatField(null=True, blank=True)
	
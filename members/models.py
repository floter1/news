from django.db import models

# Create your models here.

class Members(models.Model):
	user_name = models.CharField(max_length=250)
	age = models.IntegerField(null=True, blank=True, default=18)
	phone = models.CharField(max_length=250)
	upline = models.CharField(max_length=250)
	tin = models.CharField(max_length=250)
	points = models.FloatField(null=True, blank=True, default=0.0)
	money = models.FloatField(null=True, blank=True, default=0.0)
	photo = models.ImageField(upload_to='avatar', default='avatars/default/default.jpg')
	
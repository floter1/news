from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=250)
    writer = models.CharField(max_length=250)
    points = models.FloatField(null=True, blank=True, default=0.0)
    like = models.FloatField(null=True, blank=True, default=0.0)

class Comment(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    like = models.FloatField(null=True, blank=True, default=0.0)
    points = models.FloatField(null=True, blank=True, default=0.0)
    author = models.CharField(max_length=250)
    commentor = models.CharField(max_length=250)
    
class Bsell(models.Model):
    user_name = models.CharField(max_length=250)
    owner = models.CharField(max_length=250, default="admin")
    coins = models.FloatField(null=True, blank=True, default=0.0)
    price = models.FloatField(null=True, blank=True, default=1.0)
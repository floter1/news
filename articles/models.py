from django.db import models

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=250)
    writer = models.CharField(max_length=250)
    points = models.CharField(max_length=250)
    like = models.CharField(max_length=250)

class Comment(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=250)
    like = models.CharField(max_length=250)
    points = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    commentor = models.CharField(max_length=250)
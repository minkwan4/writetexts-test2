from django.db import models

# Create your models here.
class Writetext(models.Model):
    title = models.CharField(max_length=200)
    maintext = models.TextField()
    datetime = models.CharField(max_length=200)

class Loveskilltext(models.Model):
    title = models.CharField(max_length=200)
    maintext = models.TextField()
    datetime = models.CharField(max_length=200)

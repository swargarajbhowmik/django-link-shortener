from django.db import models

# Create your models here.

class LinksList(models.Model):
    URL = models.CharField(max_length=255)
    ShortedLink = models.CharField(max_length=255)
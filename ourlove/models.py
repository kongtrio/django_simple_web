from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Word(models.Model):
    en_name = models.CharField(max_length=50)
    cn_name = models.CharField(max_length=100)

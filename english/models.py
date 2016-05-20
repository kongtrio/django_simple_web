from __future__ import unicode_literals

from django.db import models


# python manage.py makemigrations
# python manage.py migrate
# Create your models here.
class Word(models.Model):
    en_word = models.CharField(max_length=50, null=False)
    cn_word = models.CharField(max_length=256, null=False)
    en_spell = models.CharField(max_length=256)
    sentence = models.TextField()
    more_word = models.CharField(max_length=256)
    opposites_word = models.CharField(max_length=256)

    def __unicode__(self):
        return self.en_word

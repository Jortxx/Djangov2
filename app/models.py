"""
Definition of models.
"""

from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import *

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    tema = models.CharField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    correcta = models.BooleanField(default=False)
    

class User(models.Model):
    email = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
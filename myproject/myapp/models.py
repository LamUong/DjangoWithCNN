from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from django.db import models

class PictureModel(models.Model):
    model_pic = models.ImageField()
    name = models.CharField(max_length = 50)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
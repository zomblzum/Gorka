# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class WarePost(models.Model):
    title = models.CharField(max_length=150)
    head = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    img = models.ImageField()
    info = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class ServicesPost(models.Model):
    title = models.CharField(max_length=150)
    head = models.TextField()
    sm50price = models.CharField(max_length=150)
    sm55price = models.CharField(max_length=150)
    sm60price = models.CharField(max_length=150)
    sm65price = models.CharField(max_length=150)
    sm70price = models.CharField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return self.title

class FAQPost(models.Model):
    title = models.CharField(max_length=150)
    question = models.CharField(max_length=150)
    answer = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class WarePost(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class ServicesPost(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Post(models.Model):
    img = models.ImageField()
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class FAQPost(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

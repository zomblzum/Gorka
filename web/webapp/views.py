# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'webapp/index.html')

def ware(request):
    return render(request, 'webapp/ware.html')

def services(request):
    return render(request, 'webapp/services.html')

def faq(request):
    return render(request, 'webapp/faq.html')

def contacts(request):
    return render(request, 'webapp/contacts.html')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def contacts(request):
    return render(request, 'webapp/contacts.html')
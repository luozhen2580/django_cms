# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
import json

def hello(request):
    context = {}
    context['hello'] = 'Hello World!333'
    context['list'] = [1,2,3]
    return render(request, 'hello.html', context)
    #return HttpResponse("Hello world ! ")


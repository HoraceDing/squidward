#!/usr/bin/env python

import textwrap

from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse
import textwrap
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from django.http import HttpResponseRedirect
from .forms import NameForm

# Create your views here.

def test(request):
    return HttpResponse("test passed")

    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")
    
def swag(request):
    return HttpResponse("Swag beans")
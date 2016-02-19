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

def index(request):
    response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Greetings to the world</title>
            </head>
            <body>
                <h1>Greetings to the world</h1>
                <p>Hello, world!</p>
            </body>
            </html>
        ''')
    return HttpResponse(response_text)

def test(request):
    return HttpResponse("test passed")

    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")
    
def swag(request):
    return HttpResponse("Swag beans")
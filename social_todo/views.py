#!/usr/bin/env python


from django.shortcuts import render
from django.http import HttpResponse
import textwrap
from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# Create your views here.

def index(self):
    return HttpResponse("Hello, world. You're at the tasks index.")

    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")
    
def swag(request):
    return HttpResponse("Swag beans")
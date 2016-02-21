from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader
from sensor import *

def turn(request):
	return HttpResponse("New Value Here")
	

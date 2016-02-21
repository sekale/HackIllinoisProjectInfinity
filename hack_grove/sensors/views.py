from django.shortcuts import render

from django.http import HttpResponse
from django.template import Context, loader

def turn(request):
	return HttpResponse("This is index page 1")
	

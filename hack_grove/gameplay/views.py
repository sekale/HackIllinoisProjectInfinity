from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
	#return HttpResponse("This is index page 1")
	template = loader.get_template("trial_game.html")
	return HttpResponse(template.render())


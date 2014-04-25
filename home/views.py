from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	context = RequestContext(request, {})
	return render(request, "home/index.html", context)
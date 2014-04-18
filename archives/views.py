from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from archives.models import Presenter

def index(request):
	archives_list = Presenter.objects.order_by('grad_year')
	template = loader.get_template("archives/index.html")
	context = RequestContext(request, {
		"archives_list" : archives_list,
		})
	return HttpResponse(template.render(context))

def grad_year(request, grad_year):
    return HttpResponse("You're looking at grad_year %s." % grad_year)

def presenter(request, grad_year, presenter_name):
    response = "You're looking at %s from grad_year %s."
    return HttpResponse(response % (presenter_name, grad_year))
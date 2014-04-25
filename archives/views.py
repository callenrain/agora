from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from archives.models import Presenter

def index(request):
	archives_list = Presenter.objects.order_by('grad_year')
	archives_dict = {v.grad_year:v for v in archives_list}
	context = RequestContext(request, {
		"archives_dict" : archives_dict,
	})
	return render(request, "archives/index.html", context)

def grad_year(request, grad_year):
	grad_year_archives_list = get_list_or_404(Presenter, grad_year=grad_year)
	context = RequestContext(request, {
		"grad_year_archives_list" : grad_year_archives_list,
		"year" : grad_year
	})
	return render(request, "archives/grad_year.html", context)

def presenter(request, grad_year, presenter_id):
	presenter_object = get_object_or_404(Presenter, id=presenter_id)
	context = RequestContext(request, {
		"presenter" : presenter_object,
	})
	return render(request, "archives/presenter.html", context)
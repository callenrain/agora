from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the archives index.")

def grad_year(request, grad_year):
    return HttpResponse("You're looking at grad_year %s." % grad_year)

def presenter(request, grad_year, presenter_name):
    response = "You're looking at %s from grad_year %s."
    return HttpResponse(response % (presenter_name, grad_year))
from django.conf.urls import patterns, url
from archives import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<grad_year>[0-9]+)/$', views.grad_year, name='grad_year'),
    url(r'^(?P<grad_year>[0-9]+)/(?P<nickname>\w+)/$', views.presenter, name='presenter')
)
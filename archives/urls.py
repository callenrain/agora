from django.conf.urls import patterns, url
from archives import views
from models import Presenter

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<year>[0-9]+)/$', views.YearView.as_view(), name='year'),
    url(r'^(?P<year>[0-9]+)/(?P<presenter_id>\w+)/$', views.PresenterView.as_view(), name='presenter')
)
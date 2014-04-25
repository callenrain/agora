from django.conf.urls import patterns, include, url
from django.contrib import admin
from agora import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 			include('home.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', 	include(admin.site.urls)),
    url(r'^archives/', 	include('archives.urls')),
)

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from agora import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 			include('home.urls')),
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', 	include(admin.site.urls)),
    url(r'^archives/', 	include('archives.urls')),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  
urlpatterns += patterns('',
		url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
    )

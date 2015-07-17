from django.conf.urls import patterns, include, url
from django.conf.urls.static import static


urlpatterns = patterns('',
                       url(r'^$', 'myblog.views.blogs'),
                       url(r'^get/(?P<myblog_id>\d+)/$', "myblog.views.blog"),

                       )
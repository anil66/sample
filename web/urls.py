from django.conf.urls import url, include, patterns
from django.contrib import admin
from web import models, views



urlpatterns = patterns('',
                           url(r'^admin', include(admin.site.urls)),
                url(r'^$', views.index, name='index'),
                )       

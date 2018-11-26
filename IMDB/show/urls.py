from django.conf.urls import url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'show'

urlpatterns = [
    url(r'^shows/$', views.ShowList.as_view(), name='show-list'),
    url(r'^shows/(?P<pk>[0-9]+)/$', views.ShowDetail.as_view(), name='show-detail'),
    url(r'^actor/$', views.actors_list, name='actor-list'),
    url(r'^actor/(?P<pk>[0-9]+)/$', views.ActorDetail.as_view(), name='actor-list'),

]


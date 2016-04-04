from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /postflightdata/
    url(r'^$', views.index, name='index'),
    # ex: /postflightdata/mission_name
    url(r'^missions/(?P<mission_name>)/$', views.mission, name='mission'),
    # ex: /postflightdata/identifier
    url(r'^airports/(?P<ident>\w+)', views.airport, name='ident'),
]

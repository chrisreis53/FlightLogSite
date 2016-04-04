from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /postflightdata/
    url(r'^$', views.index, name='index'),
    # ex: /postflightdata/mission_name
    url(r'^missions/(?P<mission_name>\w+)', views.mission, name='mission'),
    # ex: /postflightdata/identifier
    url(r'^airports/(?P<ident>\w+)', views.airport, name='ident'),
    # ex: /postflightdata/"pilot_name"
    url(r'^pilots/(?P<ident>\w+)', views.pilot, name='ident'),
]

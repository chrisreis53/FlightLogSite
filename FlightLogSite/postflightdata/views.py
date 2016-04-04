from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport
# Create your views here.
def index(request):
    airports = Airport.objects.order_by('pub_date')[:5]
    output = ', '.join([a.identifier for a in airports])
    return HttpResponse(airports)

def mission(request, mission_name):
    response = "You're looking at mission %s."
    return HttpResponse(response % mission_name)

def airport(request, ident):
    response = "You're looking at airport %s, with altitude %s."
    try:
        elv = Airport.objects.get(identifier=ident).elevation
        return HttpResponse(response % (ident,elv))
    except:
        response = "Airport: %s does not exist in the database."
        return HttpResponse(response % ident)

import json
from django.shortcuts import render
from django.http import JsonResponse

from maps.models import Address, Settings

# Create your views here.

'''STANDARD VIEWS'''
def index(request):
    return render(request, 'map.html')

'''API VIEWS'''

def get_mapbox_token(request):
    return JsonResponse({"token" : Settings.objects.first().mapbox_access_token})

def get_random_location(request):
    data = Address.get_random_item().to_dict()
    return JsonResponse(data)


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello from airports.');

def airport_info(request, airport_code):
    return HttpResponse('Showing info for airport: ' + airport_code)

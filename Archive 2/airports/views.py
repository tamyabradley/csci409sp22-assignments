from django.http import HttpResponse
from django.shortcuts import render
from tickets.forms import TicketForm
from tickets.models import Reservation
from .models import Airport

# Create your views here.
def index(request):
    airports = Airport.objects.all()
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)

def airport_info(request, airport_code):
    airports = Airport.objects.get(airport_code=airport_code)
    context = {'airports': airports}
    return render(request, 'airports/airport.html', context)
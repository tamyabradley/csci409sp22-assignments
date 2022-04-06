from django.http import HttpResponse
from django.shortcuts import render

import flights
from .models import Flights # Import Flight model
from airports.models import Airport # Import airport model to get airport id and code
from .forms import FlightForm

def index(request):
    # Create an instance of the form class
    form = FlightForm()
    # Render the form
    return render(request, 'flight/index.html', {'form': form})

def flight_search(request, origin, destination):
        origin = Airport.objects.get(airport_code=origin)
        destination = Airport.objects.get(airport_code=destination)
    # Code to select flights from the database
    #   flights = Flights.objects.filter(origin_id=origin, destination_id=destination)

        flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flights])
        return HttpResponse('Showing flights: ' + flight_list)

def search(request, flights, destination=None, origin=None):
    form = FlightForm(request.POST)
    if form.is_valid():
        # extract the origin and airport code from the form
        origin = Airport.objects.get(airport_code=origin)
        destination = Airport.objects.get(airport_code=destination)
        # Select flights from dataabase
        flights = Flights.objects.filter(origin=origin.id, destination=destination.id)

        flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                                 f.airline.airline_code for f in flights])

        # Render response
        return render(request, 'flight/flight_search.html', {'flights': flights})
from django.http import HttpResponse
from .models import Flights # Import Flight model
from airports.models import Airport # Import airport model to get airport id and code

def index(request):
    # Fetch all flights
    flights = Flights.objects.all()
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code for f in flights])
    return HttpResponse('Listing all flights: ' + flight_list)

def flight_search(request, origin, destination):
    origin = Airport.objects.get(airport_code=origin)
    destination = Airport.objects.get(airport_code=destination)
    # Code to select flights from the database
    flights = Flights.objects.filter(origin_id=origin, destination_id=destination)

    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flights])
    return HttpResponse('Showing flights: ' + flight_list)



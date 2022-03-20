from django.http import HttpResponse
from .models import Airport
# Create your views here.
def index(request):
    airports = Airport.objects.all()
    airport_list = ', '.join([a.airport_code for a in airports])
    return HttpResponse('Showing all airports: ' + airport_list);

def airport_info(request, airport_code):
    airport = Airport.objects.get(airport_code=airport_code)
    return HttpResponse('Showing info for airport: ' + airport.name + "- " + airport.airport_code)

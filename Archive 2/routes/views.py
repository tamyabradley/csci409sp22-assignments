from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello from routes.');

def route_search(request, origin, destination):
    return HttpResponse('Showing routes from ' + origin + ' to ' + destination)

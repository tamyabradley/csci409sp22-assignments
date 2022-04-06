from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('Hello from tickets.');

def ticket_search(request, confirmation_number):
    return HttpResponse('Showing tickets for the confirmation number: ' + confirmation_number)

from django.http import HttpResponse
from django.shortcuts import render
from .models import Reservation
from .forms import TicketForm

def index(request):
    # Create the instance of the form class
    form = TicketForm()
    # Render the form
    return render(request, 'tickets/index.html', {'form': form})

def search(request, confirmation_number=None):
    form = TicketForm(request.POST)
    if form.is_valid():
        reservation = Reservation.objects.get(id=form.cleaned_data[confirmation_number])
        return render(request, 'tickets/ticket_search.html', {'reservation': reservation})
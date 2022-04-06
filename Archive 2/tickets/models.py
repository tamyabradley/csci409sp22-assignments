from django.db import models
from flights.models import Flights

# Create your models here.

class Reservation(models.Model):
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    num_people = models.IntegerField()
    total_cost = models.DecimalField(max_digits=5, decimal_places=2)

class Tickets(models.Model):
    # Runway Designation
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    MAIN_CABIN = 'M'

    TICKET_CHOICES = [
        (FIRST_CLASS, 'First Class'),
        (BUSINESS_CLASS, 'Business Class'),
        (MAIN_CABIN, 'Main Cabin'),
    ]
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    seat = models.CharField(max_length=10)
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    ticket_class = models.CharField(max_length=1)
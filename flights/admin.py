from django.contrib import admin
from .models import Flights, Airline

#Register your model here.
class AirlineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['airline_name', 'airline_code']})
    ]

class FlightInline(admin.StackedInline):
    model = Flights #Specify which model to use
    extra = 2 #How many to start with

#Register your model here.
class FlightAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Airline Information', {'fields': ['airline', 'flight_number']}),
        ('Orgin/Destination', {'fields': ['origin', 'destination']}),
        ('Departure and Arrival Time', {'fields': ['departure', 'arrival'], 'classes': ['collapse']})

    ]

inlines = [FlightInline]  # Load the Flight Class
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flights, FlightAdmin)
from django.contrib import admin
from .models import Reservation, Tickets

#Register your model here.
class TicketInline(admin.StackedInline):
    model = Tickets #Specify which model to use
    extra = 2


class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['flight', 'num_people', 'total_cost']})
                     ]
    inlines = [TicketInline]
admin.site.register(Reservation, ReservationAdmin)

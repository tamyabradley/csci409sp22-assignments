# Load path from django.urls
from django.urls import path
# Load this applications views.py file
from . import views

# Define url patterns
urlpatterns = [
    # Get index value
    # Example url: /airports/
    path('/', views.index),
    # Show Airport info
    # Example url /airports/MYR
    # NOTICE: the airport_code parameter in the url matches
    #    the parameter in the airport_info fUnction
path('/<str:confirmation_number>/', views.ticket_search),
]
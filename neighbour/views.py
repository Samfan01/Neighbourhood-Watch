from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    title = 'Welcome to the Neighbourhood'
    template_name = 'home.html'
    neighbourhoods = NeighbourHood.objects.all()
    
    return render(request,template_name,{'title':title,'neighbourhoods':neighbourhoods})
from django.shortcuts import render

# Create your views here.

def home(request):
    title = 'Welcome to the Neighbourhood'
    template_name = 'home.html'
    
    return render(request,template_name,{'title':title})
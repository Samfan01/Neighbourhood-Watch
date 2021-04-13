from django.shortcuts import render,redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    title = 'Welcome to the Neighbourhood'
    template_name = 'home.html'
    neighbourhoods = NeighbourHood.objects.all()
    
    return render(request,template_name,{'title':title,'neighbourhoods':neighbourhoods})

def profile(request):
    template_name = 'profile.html'
    
    
    
    return render(request,template_name)


def update_profile(request):
    model = Profile
    form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            post = form.save(commit=False)      
            post.save()
        return redirect('profile')
    else:
        form = ProfileForm
   
    template_name = 'update_profile.html',
    
    return render(request,template_name,{'form':form})

def hood(request,neighbourhood_id):
    neighbourhoods = get_object_or_404(NeighbourHood, id=neighbouhood_id)
    user = request.user.profile
    template_name = 'hood.html'
    
    return render(request,template_name)
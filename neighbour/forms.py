from django import forms
from . models import *



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email','name','profile_pic')
        
        widgets = {
            'email': forms.TextInput(attrs = {'class': 'form-control'}),
            'name': forms.TextaInput(attrs = {'class': 'form-control'}),
        }
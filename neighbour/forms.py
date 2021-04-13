from django import forms
from . models import *



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email','name','profile_pic')
        
        widgets = {
            'email': forms.TextInput(attrs = {'class': 'form-control'}),
            'name': forms.TextInput(attrs = {'class': 'form-control'}),
        }
        
class PostForm(forms.ModelForm):
    model = Post
    fields = ('post_title','post_image','post_description')
    
    widgets = {
           'post_title':forms.TextInput(attrs = {'class':'form-control'}),
           'post_description':forms.TextInput(attrs = {'class':'form-control'}),
    }
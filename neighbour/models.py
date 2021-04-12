from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.
class Neighbourhood(models.Model):
    neighbouhood_name = models.CharField(max_length = 90)
    neighbouhood_location = models.CharField(max_length = 90)
    occupants = models.CharField(max_length = 90)

    def __str__(self):
        return self.neighbouhood_name
    
    def create_neighbourhood(self):
        self.save()
        
    def delete_neighbourhood(self):
        self.delete()
        

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length = 90)
    email = models.EmailField()
    neighbouhood_id = models.ForeignKey('NeighbourHood',on_delete=models.CASCADE,related_name = 'profile')
    
    @receiver(post_save, sender=User)
    def user_profile(sender,instance,created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
            
    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ['email']
        
    def save_profile(self):
        self.save()
    
    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

class Post(models.Model):
    post_title = models.CharField(max_length = 90)
    post_description = models.TextField()
    post_image = models.ImageField(upload_to = 'neighbour/')
    post_date = models.DateTimeField(auto_now_add =True)        
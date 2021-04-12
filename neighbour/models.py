from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(Max_length = 60)
    email = models.EmailField()
    neighbouhood_id = models.ForeignKey('NeighbourHood',on_delete=models.CASCADE,related_name = 'profile')
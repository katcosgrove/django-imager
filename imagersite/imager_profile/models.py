from django.db import models
from multiselectfield import MultiSelectField  

# Create your models here.


class ImagerProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    location = 
    website = 
    fee = 
    camera = 

    services = 

    photostyles = 

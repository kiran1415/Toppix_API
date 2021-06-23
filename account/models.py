from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


USER_TYPE = (
    ('CB', 'Contributer'),
    ('BY', 'Buyer'),
    ('AD', 'Admin'),
    

)



class UserProfile(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=30,null=True,blank=True)
    country = models.CharField(max_length=30,null=True,blank=True)
    state = models.CharField(max_length=30,null=True,blank=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=10 , null=True , blank=True)
    ip = models.CharField(max_length=200, null=True, blank=True)
    referralby = models.CharField(null=True , blank=True , max_length=50)


    def __str__(self):
        return self.name





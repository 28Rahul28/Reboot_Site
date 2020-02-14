from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
categories = ('Accomodation', 'Travel',)

class User(AbstractUser):
    email = models.EmailField( blank=False,max_length=254, verbose_name='email address')
    is_Service_provider = models.BooleanField(default=False)
    is_Verified = models.BooleanField(default=False)
    license_data = models.CharField(max_length=264)
    license_file = models.FileField(upload_to='',)


class Events(models.Model):
    title = models.CharField(max_length=264)
    description = models.TextField()
    #thumbnail = models.ImageField(upload_to='thumbnail/',)
    features = models.TextField()
    category = models.QuerySet(query=categories)
    price = models.IntegerField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='events')
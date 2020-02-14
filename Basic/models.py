from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
categories = ((1, 'Accomodation'),(2, 'Travel'),)

class User(AbstractUser):
    email = models.EmailField( blank=False,max_length=254, verbose_name='email address')
    is_Service_provider = models.BooleanField(default=False)
    is_Verified = models.BooleanField(default=False)
    license_data = models.CharField(max_length=264)
    license_file = models.FileField(upload_to='',)


class Events(models.Model):
    title = models.CharField(max_length=264)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/',)
    features = models.TextField()
    category = models.CharField(choices=categories, max_length=264)
    price = models.IntegerField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='events')
    location = models.CharField(max_length=264)
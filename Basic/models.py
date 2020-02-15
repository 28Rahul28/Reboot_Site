from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
categories = ((1, 'Home Stay'),(2, 'Transport'),(3,'Travel Agency'),(4,'Restaurant'),(5, 'Ayurvedha'),(6,'other'))

class User(AbstractUser):
    email = models.EmailField( blank=False,max_length=254, verbose_name='email address')
    is_Service_provider = models.BooleanField(default=False)
    is_Verified = models.BooleanField(default=False)
    license_data = models.CharField(max_length=264)
    license_file = models.FileField(upload_to='',)
    def __str__(self):
        return self.username


class Events(models.Model):
    title = models.CharField(max_length=264)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/',)
    keywords = models.TextField()
    category = models.IntegerField(choices=categories,  default=1)
    price = models.IntegerField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='events')
    location = models.CharField(max_length=264,default='kerala')


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateTimeField()


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
    features = models.TextField()
    category = models.IntegerField(choices=categories, max_length=264, default=1)
    price = models.IntegerField(null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='events')
    location = models.CharField(max_length=264,default='kumarakom')
    def __str__(self):
        return (categories[int(self.category)][1])

class Comment(models.Model):
    event = models.ForeignKey(Events,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.body

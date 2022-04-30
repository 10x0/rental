from distutils.command.upload import upload
from enum import auto
from django.db import models
from users.models import User

# Create your models here.

class VehicleImage(models.Model):
    image = models.ImageField(upload_to='vehicles/',null=True)

    def __str__(self):
        return self.image.url

VEHICLE_TYPES = (
        ('Car', 'Car'),
        ('Bike', 'Bike'),
    )


class Vehicle(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField()
    daily_rate = models.IntegerField()
    type = models.CharField(choices=VEHICLE_TYPES,max_length=20)
    images = models.ManyToManyField(VehicleImage,related_name='vehicle_images', blank=True, default=None)
    on_rent = models.BooleanField(default=False)
    provider = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    pickup_time = models.DateTimeField(auto_now=True)
    days = models.IntegerField(default=1)
    payment = models.IntegerField()

    def __str__(self):
        return str(self.pickup_time)
from django.contrib import admin
from django.contrib.auth.models import Group
from main.models import Booking, Vehicle, VehicleImage

# Register your models here.
admin.site.unregister(Group)
admin.site.register(VehicleImage)
admin.site.register(Vehicle)
admin.site.register(Booking)
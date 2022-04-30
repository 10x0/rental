from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render

from .models import  Booking, Vehicle, VehicleImage
from django.contrib.auth.decorators import login_required
from .decorators import provider, rider
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

@login_required
@provider
def provider_home(request):
    vehicles = Vehicle.objects.filter(provider=request.user)
    return render(request,'provider/home.html',{'vehicles':vehicles})

def vehicles(request):
    vehicles = Vehicle.objects.filter(type='Car')[:6]
    if request.method == "POST":
        name = request.POST["query"]
        type = request.POST["type"]
        if name=="":
            vehicles = Vehicle.objects.filter(type=type)[:6]
        else:
            vehicles = Vehicle.objects.filter(name__icontains=name,type=type)[:6]
        if len(vehicles) == 0:
            messages.error(request,"No items found.")
    return render(request,'rider/vehicles.html',{'vehicles':vehicles})

@login_required
@rider
def bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request,'rider/bookings.html',{'bookings':bookings})

@login_required(login_url='main:redirect_login')
@rider
def book(request,id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method =='POST':
        pickup_date = request.POST.get('pickup_date')
        return_date = request.POST.get('return_date')
        pickup_date = datetime.strptime(pickup_date,'%Y-%m-%d')
        return_date = datetime.strptime(return_date,'%Y-%m-%d')
        # if pickup_date >= return_date or pickup_date<datetime.now():
        #     messages.error(request,'Invalid date.')
        #     return redirect('main:book',id=id)
        days = (return_date - pickup_date).days
        booking = Booking()
        booking.user = request.user
        booking.vehicle = vehicle
        booking.days = days
        booking.payment = vehicle.daily_rate * days
        booking.save()
        return redirect('main:bookings')
    return render(request,'rider/book.html',{'vehicle':vehicle})

@login_required
@provider
def add_vehicle(request):
    if request.method == "POST":
        name = request.POST['name']
        type = request.POST['type']
        daily_rate = request.POST['daily_rate']
        year = request.POST['year']
        provider = request.user
        vehicle = Vehicle(
            name=name,
            type=type,
            daily_rate=daily_rate,
            year=year,
            provider=provider
        )
        vehicle.save()
        if len(request.FILES) != 0:
            for img in request.FILES.getlist('images'):
                image = VehicleImage(image=img)
                image.save()
                vehicle.images.add(image)

        return redirect('main:provider') 
        
    return render(request,'provider/add_vehicle.html')

def remove_vehicle(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)
    if request.user == vehicle.provider:
        vehicle.delete()
        return redirect('main:provider')
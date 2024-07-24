from django.shortcuts import render
from .models import CabsOnlineForm, City, Trips
from django.contrib import messages

# Create your views here.

def index(request):
    cabform = CabsOnlineForm()
    loc = City.objects.all()
    if request.method == "POST":
        cabform.customer_name = request.POST.get("name")
        cabform.customer_email = request.POST.get("email")
        cabform.mo_no = request.POST.get("phone")
        cabform.cab_type = request.POST.get("type")
        cabform.from_destination = request.POST.get("from")
        cabform.to_destination = request.POST.get("to")
        cabform.journey_date = request.POST.get("date")
        cabform.journey_time = request.POST.get("time")

        cabform.save()
        messages.success(request,"Thank You for making Reservation, Our team will contact you soon!")

    return render(request,"index.html",{"loc":loc})

def trips(request):
    row = Trips.objects.all()
    return render(request,"trips.html",{"row":row})
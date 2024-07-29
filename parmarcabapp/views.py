from django.shortcuts import render
from .models import CabsOnlineForm, City, Trips
from django.contrib import messages
from heyoo import WhatsApp
import requests
import json
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

        # Send WhatsApp message using WhatsApp Business API
        whatsapp_api_url = "https://graph.facebook.com/v13.0/YOUR_PHONE_NUMBER_ID/messages"
        access_token = "YOUR_ACCESS_TOKEN"

        message_body = (
            f"Thank you for making a reservation, {cabform.customer_name}!\n"
            f"Your journey details:\n"
            f"From: {cabform.from_destination}\n"
            f"To: {cabform.to_destination}\n"
            f"Date: {cabform.journey_date}\n"
            f"Time: {cabform.journey_time}\n"
            "Our team will contact you soon!"
        )

        payload = {
            "messaging_product": "whatsapp",
            "to": f"{cabform.mo_no}",
            "type": "text",
            "text": {
                "body": message_body
            }
        }
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        response = requests.post(whatsapp_api_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            messages.success(request, "Thank You for making a Reservation, Our team will contact you soon!")
        else:
            messages.error(request, "Failed to send WhatsApp message. Please try again later.")

    return render(request, "index.html", {"loc": loc})


def trips(request):
    row = Trips.objects.all()
    return render(request,"trips.html",{"row":row})

def gallary(request):
    return render(request,"gallery.html")
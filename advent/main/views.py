from django.shortcuts import render, redirect
from .models import ContactInquiry, BookingInquiry

# Create your views here.
def home(request):
  return render(request, 'index.html')

def contact_view(request):

    if request.method == "POST":

        ContactInquiry.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        return redirect("contact")

    return render(request, "contact.html")

def info(request):
    return render(request, "info.html")

def locations(request):
    return render(request, "locations.html")

def package(request):
    return render(request, "package.html")

def booking_view(request):

    if request.method == "POST":

        BookingInquiry.objects.create(

            first_name=request.POST.get("firstname"),
            last_name=request.POST.get("lastname"),

            email=request.POST.get("email"),
            phone=request.POST.get("phone"),

            checkin=request.POST.get("checkin"),
            checkout=request.POST.get("checkout"),

            accommodation=request.POST.get("accommodation"),

            rooms=request.POST.get("rooms"),

            room_type=request.POST.get("room_type"),

            additional=request.POST.get("additional"),
        )

        return redirect("booking")
    
    return render(request, "booking.html")







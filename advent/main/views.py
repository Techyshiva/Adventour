from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def home(request):
  return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        return redirect("contact")  # or any success page

    return render(request, "contact.html")

def info(request):
    return render(request, "info.html")

def locations(request):
    return render(request, "locations.html")

def package(request):
    return render(request, "package.html")

def booking(request):
    return render(request, "booking.html")
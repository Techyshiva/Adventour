from django.db import models

# create your models here

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class BookingInquiry(models.Model):

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    checkin = models.DateField(null=True, blank=True)
    checkout = models.DateField(null=True, blank=True)

    accommodation = models.CharField(max_length=100, null=True, blank=True)

    rooms = models.IntegerField(null=True, blank=True)

    room_type = models.CharField(max_length=50, null=True, blank=True)

    additional = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    

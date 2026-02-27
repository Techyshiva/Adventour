from django.contrib import admin
from .models import ContactInquiry, BookingInquiry


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "subject",
    )

    list_filter = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20



@admin.register(BookingInquiry)
class BookingInquiryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "accommodation",
        "checkin",
        "checkout",
        "created_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "accommodation",
    )

    list_filter = (
        "accommodation",
        "checkin",
        "checkout",
        "created_at",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20
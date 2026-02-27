from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('info/', views.info, name='info'),
    path('locations/', views.locations, name='locations'),
    path('package/', views.package, name='package'),    
    path("contact/", views.contact_view, name="contact"),
    path("booking/", views.booking_view, name="booking"),  
    
]

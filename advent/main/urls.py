from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('contact/', views.contact, name='contact'),
    path('info/', views.info, name='info'),
    path('locations/', views.locations, name='locations'),
    path('package/', views.package, name='package'),
    path('booking/', views.booking, name='booking'),
    
]

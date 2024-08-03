from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about-us/',about,name="about-us"),
    path('termsandconditions/',termsandconditions,name="termsandconditions"),
    path('privacy/',privacy,name="privacy"),
    path('contact-us/',contact,name="contact-us")
]

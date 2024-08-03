from django.shortcuts import render,redirect
from django.contrib import messages
from .models import contactus

# Create your views here.
def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about-us.html')

def termsandconditions(request):
    return render(request,"termsandconditions.html")

def privacy(request):
    return render(request,"privacy.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        contact=contactus(name=name,email=email,message=message)
        contact.save()

        messages.success(request,"Message Sent Successfully")
        return redirect('/contact-us/')
    
    return render(request,"contact-us.html")
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about-us.html')

def termsandconditions(request):
    return render(request,"termsandconditions.html")
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'dashboard.html',{"total_visits":100})
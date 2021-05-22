import intern
from django.shortcuts import render
from django.http import HttpResponse

from .models import Country

# Create your views here.
def home(request):
    countries = Country.objects.all()
    print("this is the data we get",request.GET)
    return render(request,'intern/home.html', {'countries': countries})

def about(request):
    return render(request,'intern/about.html')
    

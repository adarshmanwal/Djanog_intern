from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    countries = ['India']
    return render(request,'intern/home.html', {'countries': countries})

def about(request):
    return render(request,'intern/about.html')
    

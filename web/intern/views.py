from django.shortcuts import render
from django.http import HttpResponse

from geosky import geo_plug

# Create your views here.
def home(request):
    countries = geo_plug.all_CountryNames()
    # states = geo_plug.all_Country_StateNames()
    # print(states);
    return render(request,'intern/home.html', {'countries': countries})

def about(request):
    return render(request,'intern/about.html')
    

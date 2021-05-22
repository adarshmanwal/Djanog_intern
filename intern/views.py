import intern
from django.shortcuts import render
from django.http import HttpResponse

from .models import Country, Post, State, City

# Create your views here.
def home(request):
    countries = Country.objects.all()
    if request.method=="POST":
        print("all data is hear" ,request.POST)
        name=request.POST['Your_name']
        birthdate=request.POST['birthDate']
        country=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        ins=Post(name=name,birthDate=birthdate,country=country,state=state,city=city)
        ins.save()
        
    # print("this is the data we get",request.POST)
    return render(request,'intern/home.html', {'countries': countries})

#  to populate state dropdown when country is selected.
def state_view(request, id):
    states = State.objects.filter(country_id=id)
    return render(request,'intern/state.html', {'states': states})

#  to populate city dropdown when state is selected.
def city_view(request,id):
    cities = City.objects.filter(state_id=id)
    return render(request, 'intern/city.html', {'cities': cities})

def about(request):
    return render(request, 'intern/about.html')
    

import intern
from django.shortcuts import render
from django.http import HttpResponse

from .models import Country, Post, State, City

# Create your views here.
def home(request):
    countries = Country.objects.all()
    success = 0
    error = 0
    if request.method=="POST":
        name=request.POST['Your_name'].strip()
        birthdate=request.POST['birthDate'].strip()
        country=request.POST['country'].strip()
        state=request.POST['state'].strip()
        city=request.POST['city'].strip()
        if(name == '' or birthdate == '' or country == '' or state == '' or city == '' ):
            error = 1
        else:
            ins=Post(name=name,birthDate=birthdate,country=country,state=state,city=city)
            ins.save()
            success = 1

    # print("this is the data we get",request.POST)
    return render(request,'intern/home.html', {'countries': countries, 'success': success, 'error': error})

#  to populate state dropdown when country is selected.
def state_view(request, name):
    country = Country.objects.get(name=name)
    states = State.objects.filter(country_id=country.id)
    return render(request,'intern/state.html', {'states': states})

#  to populate city dropdown when state is selected.
def city_view(request, name):
    state = State.objects.get(name=name)
    cities = City.objects.filter(state_id=state.id)
    return render(request, 'intern/city.html', {'cities': cities})

# List of persons
def persons_view(request):
    persons = Post.objects.all()
    return render(request, 'intern/persons.html', {'persons': persons})

def about(request):
    return render(request, 'intern/about.html')


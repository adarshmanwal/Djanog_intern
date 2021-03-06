from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='intern-home'),
    path('country/<name>', views.state_view,name='intern-state'),
    path('state/<name>', views.city_view,name='intern-city'),
    path('persons/',views.persons_view,name='intern-persons'),
    path('about/',views.about,name='intern-about')
]
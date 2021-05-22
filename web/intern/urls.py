from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='intern-home'),
    path('about/',views.about,name='intern-about')
]
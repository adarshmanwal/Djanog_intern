from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='intern-home'),
    path('country/<int:id>', views.state_view,name='intern-state'),
    path('state/<int:id>', views.city_view,name='intern-city'),
    path('about/',views.about,name='intern-about')
]
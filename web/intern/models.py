from django.db import models

# Create your models here.
class Post(models.Model):
    name=models.CharField(max_length=1000)
    birthDate=models.CharField(max_length=1000)
    country=models.CharField(max_length=1000)
    state=models.CharField(max_length=1000)
    city=models.CharField(max_length=1000)



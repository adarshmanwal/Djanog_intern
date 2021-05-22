from django.db import models

class Post(models.Model):
    name=models.CharField(max_length=1000)
    birthDate=models.CharField(max_length=1000)
    country=models.CharField(max_length=1000)
    state=models.CharField(max_length=1000)
    city=models.CharField(max_length=1000)

class Country(models.Model):
    id=models.IntegerField(primary_key=True)
    sortname=models.CharField(max_length=5)
    name=models.CharField(max_length=1000)
    phonecode=models.CharField(max_length=20)

class State(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=1000)
    country_id=models.IntegerField()

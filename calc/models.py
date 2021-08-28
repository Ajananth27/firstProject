from django.db import models

# Create your models here.

class feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comments = models.TextField()

class hospitallist(models.Model):
    hospitalname = models.CharField(max_length=50)
    hospital = models.CharField(max_length=15)
    specialty = models.CharField(max_length=10)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    district = models.CharField(max_length=15)
    state = models.CharField(max_length=10)
    contactno = models.IntegerField()
    mailid = models.EmailField()
    location = models.TextField()

class covidreport(models.Model):
    country = models.CharField(max_length=30)
    totalcases = models.CharField(max_length=20)
    newcases = models.CharField(max_length=20)
    totaldeaths = models.CharField(max_length=20)
    newdeaths = models.CharField(max_length=10)
    totalrecovered = models.CharField(max_length=20)
    newrecovered = models.CharField(max_length=10)
    activecases = models.CharField(max_length=15)
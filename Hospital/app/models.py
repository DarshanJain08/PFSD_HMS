from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Person(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)


class Doctor(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30)
    experience = models.IntegerField()
    degree = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname+" "+self.lastname

class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    timing = models.CharField(max_length=30)
    description = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    msg = models.TextField()


class Reports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    pname = models.CharField(max_length=50)
    page = models.IntegerField()
    pemail = models.EmailField(max_length=50)
    pphone = models.CharField(max_length=20)
    pgender = models.CharField(max_length=20)
    pdiagnosis = models.TextField()
    pprescription = models.TextField()
    doctorname = models.CharField(max_length=50)
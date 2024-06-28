from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Person, Doctor, Appointment, Contact, Reports


def home(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def checklogin(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        doctor = Doctor.objects.get(username=username, password=password)
        doctor_id = doctor.pk
        return redirect('doctorhome', doctor_id=doctor_id)
    except Doctor.DoesNotExist:
        try:
            person = Person.objects.get(username=username, password=password)
            return redirect('personhome', username=username)
        except Person.DoesNotExist:
            messages.error(request,"Login failed")
            return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        person=Person(firstname=firstname,lastname=lastname,email=email,username=username,password=password)
        person.save()
        return redirect('login')
    return render(request, 'signup.html')


def doctorhome(request, doctor_id):
    return render(request, 'doctor_home.html', {"doctor_id": doctor_id})

def personhome(request, username):
    return render(request, 'person_home.html', {"username": username})


def bookappointment(request,username):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        doctor_id = request.POST.get('doctorname')
        date = request.POST.get('date')
        timing = request.POST.get('timing')
        description = request.POST.get('description')

        try:
            doctor = Doctor.objects.get(pk=doctor_id)
        except Doctor.DoesNotExist:
            messages.error(request, 'Selected doctor does not exist.')
            return redirect('bookappointment', username=username)

        appointment = Appointment(name=name, email=email, doctor=doctor, date=date, timing=timing,
                                  description=description)
        appointment.save()
        messages.success(request,"Successfully booked")
        return redirect('bookappointment', username=username)
    else:
        doctors = Doctor.objects.all()
        return render(request, 'appointment.html', {'doctor_names': doctors,'username':username})


def doctors(request,username):
    doctorlist=Doctor.objects.all()
    return render(request,'doctors.html',{'doctorlist':doctorlist, 'username': username})


def contact(request,username):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        contact = Contact(name=name,email=email,phone=phone,msg=msg)
        contact.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact',username=username)
    return render(request,'contact.html',{'username':username})


def viewappointments(request,doctor_id):
    print(doctor_id)
    try:
        doctor = Doctor.objects.get(pk=doctor_id)
        appointments = Appointment.objects.filter(doctor=doctor)
        return render(request, 'viewappointments.html', {'doctor':doctor,'appointments': appointments,'doctor_id': doctor_id})
    except Doctor.DoesNotExist:
        return render(request, 'doctor_home.html')


def submitreport(request,doctor_id):
    if request.method=='POST':
        pname=request.POST.get('pname')
        page=request.POST.get('page')
        pemail=request.POST.get('pemail')
        pphone=request.POST.get('pphone')
        pgender=request.POST.get('pgender')
        pdiagnosis=request.POST.get('pdiagnosis')
        pprescription=request.POST.get('pprescription')
        doctorname=request.POST.get('doctorname')
        report=Reports(pname=pname,page=page,pemail=pemail,pphone=pphone,pgender=pgender,pdiagnosis=pdiagnosis,pprescription=pprescription,doctorname=doctorname)
        report.save()
        messages.success(request,"Successfully submitted report")
        return redirect('submitreport',doctor_id=doctor_id)
    return render(request,'submitreport.html',{'doctor_id':doctor_id})


def viewreports(request,username):
    person = get_object_or_404(Person, username=username)
    reports = Reports.objects.filter(pemail=person.email)
    return render(request,'viewreports.html',{'username':username, 'reports': reports})
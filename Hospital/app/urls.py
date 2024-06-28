from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login,name='login'),
    path('logout/', views.logout,name='logout'),
    path('checklogin/', views.checklogin,name='checklogin'),
    path('signup/', views.signup,name='signup'),
    path('doctorhome/<int:doctor_id>/', views.doctorhome, name='doctorhome'),
    path('<str:username>/personhome/', views.personhome, name='personhome'),
    path('<str:username>/bookappointment/', views.bookappointment,name='bookappointment'),
    path('<str:username>/doctors/', views.doctors,name='doctors'),
    path('<str:username>/contact/', views.contact,name='contact'),
    path('doctor/<int:doctor_id>/viewappointments/', views.viewappointments, name='viewappointments'),
    path('doctor/<int:doctor_id>/submitreport/', views.submitreport, name='submitreport'),
    path('<str:username>/viewreports/',views.viewreports,name='viewreports'),

]

from calc import views
from django.urls import path
from calc import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.login, name= 'login'),
    path('logout', views.logout, name= 'logout'),
    path('register', views.registration, name= 'registration'),
    path('adminInserts', views.adminInserts, name = 'adminInserts'),
    path('adminInserts/search/', views.searchMain, name='searchMain'),
    path('adminInserts/insert/', views.insertadminrecord, name='insertadminrecord'),
    path('adminInserts/retrieve/', views.adminretrieve, name='adminretrieve'),
    path('adminInserts/retrieve/hospital', views.searchhospital, name='searchhospital'),
    path('adminInserts/retrieve/<int:id>', views.editadminrecord, name='editadminrecord'),
    path('adminInserts/retrieve/delete/<int:id>', views.deleterecord, name='deleterecord'),
    path('feedback', views.insertFBrecord, name='insertFBrecord'),

    path('search/<str:speciality>/', views.searcheye, name='searcheye'),
    path('search/heart/<int:id>/', views.getlocation, name='getlocation'),

    path('covidcase', views.covidcase, name='covidcase'),
    path('country/chart/', views.searchcountry, name='searchcountry'),
    path('country/get/', views.chartdatamax, name='chartdatamax'),
]
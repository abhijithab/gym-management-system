from django.urls import path

from homepage import views

app_name='homepage'

urlpatterns =[


    path('about/',views.about,name='about'),

    path('home/', views.home, name='home'),

    path('class/', views.classdetails, name='classdetails'),

    path('services/', views.services, name='services'),

    path('team/', views.team, name='team'),

    path('contact/', views.contact, name='contact'),

    path('timetable/', views.timetable, name='timetable'),

    path('calculator/', views.calculator, name='calculator'),

    path('gallery/', views.gallery, name='gallery'),

    path('blog/', views.blog, name='blog'),

    path('404/', views.error, name='error'),


]
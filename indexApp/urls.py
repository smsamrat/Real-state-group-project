from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),

    #properties url
    path('landProject/',views.land_project, name='land_project'),
    path('apnartmentProject/',views.apartment_project, name='apartment_project'),

    #service url
    path('service/',views.service, name='service'),

    #blog url
    path('blog/',views.blog, name='blog'),

    #about url
    path('about/',views.about, name='about'),

    #gallay url
    path('gallery/',views.gallay, name='gallery'),
]
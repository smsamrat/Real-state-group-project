from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),

    #properties url
    path('landProject/',views.land_project, name='land_project'),
    path('apnartmentProject/',views.apartment_project, name='apartment_project'),
    path('details/property/<str:id>/',views.details_property, name='details_property'),

    #service url
    path('service/',views.service, name='service'),

    #blog url
    path('blog/',views.blog, name='blog'),

    #about url
    path('about/',views.about, name='about'),

    #gallay url
    path('gallery/',views.gallay, name='gallery'),
    path('video/',views.video, name='video'),

    #get_in_touch
    path('career/',views.career, name='career'),
    path('contact/',views.contact, name='contactus'),
    path('notice/',views.notice, name='notice'),
    path('our_team/',views.our_team, name='ourteam'),



]
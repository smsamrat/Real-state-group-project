from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('location-post/<str:location_name>/',views.location, name='location'),
    path('feature-details-property/<str:id>/',views.feature_details_property, name='feature_details_property'),
    path('recent-details-property/<str:id>/',views.recent_details_property, name='recent_details_property'),

    #properties url
    path('landProject/',views.land_project, name='land_project'),
    path('recent-details-property/<str:id>/',views.land_details_property, name='land_details_property'),
    path('apnartmentProject/',views.apartment_project, name='apartment_project'),
    path('details/property/<str:id>/',views.apartment_details_property, name='details_property'),

    #service url
    path('service/',views.service, name='service'),

    #blog url
    path('blog/',views.blogs, name='blog'),
    path('read/more/<str:id>/',views.readMore, name='read-more'),

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

    path('our-team', views.our_team, name='ourteam'),
    path('contact', views.contact, name='contactus'),
    path('career', views.career, name='career'),
    path('career-detail/<slug>', views.career_detail, name='career-detail'),
    path('notice', views.notice, name='notice'),
    # path('about-us', views.about_us, name='about-us'),



]
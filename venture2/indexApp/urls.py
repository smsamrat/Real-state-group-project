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
    path('land-details-property/<str:id>/',views.land_details_property, name='land_details_property'),
    path('apnartmentProject/',views.apartment_project, name='apartment_project'),
    path('details/property/<str:id>/',views.apartment_details_property, name='details_property'),
    path('product/filter-data',views.filter_data,name="filter-data"),

    # path('dropdown/filter-dropdown',views.filter_dropdown,name="filter-dropdown"),

    path('get-district-ajax/', views.get_district_ajax, name="get_district_ajax"),
    path('get-area-ajax/', views.get_area_ajax, name="get_area_ajax"),

    #service url
    # path('service/',views.service, name='service'),
    path('service/venture-rending/',views.venture_trending, name='venture_rending'),
    path('service/Venture-Security',views.Venture_Security, name='Venture_Security'),
    path('service/Venture-design-Development/',views.Venture_design_Development, name='Venture_design_Development'),
    path('service/Venture-it',views.Venture_it, name='Venture_it'),
    path('service/Venture-tourism/',views.Venture_tourism, name='Venture_tourism'),
    path('service/details-page/<str:id>/',views.service_details, name='service_details'),

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
    path('career-detail/<slug>-<str:id>/', views.career_detail, name='career-detail'),
    path('notice', views.notice, name='notice'),
    # path('about-us', views.about_us, name='about-us'),

    #booking now
    path('booking-now', views.booking_now, name='booking_now'),
    



]
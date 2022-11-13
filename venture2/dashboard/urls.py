from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('propert-add',property_add, name='property_add'),
    path('propert-view',property_view, name='property_view'),
    path('propert-edit/<str:id>/',property_edit, name='property_edit'),
    path('propert-delete/<str:id>/',property_delete, name='property_delete'),

    #why chose us
    path('why-choose-us-add/',why_choose_us_add, name='why_choose_us_add'),
    path('why-choose-us-view/',why_choose_us_view, name='why_choose_us_view'),
    path('why-choose-us-edit/<str:id>/',why_choose_us_edit, name='why_choose_us_edit'),
    path('why-choose-us-delete/<str:id>/',why_choose_us_delete, name='why_choose_us_delete'),

    #Faq
    path('faq-add/',faq_add, name='faq_add'),
    path('faq-view/',faq_view, name='faq_view'),
    path('faq-edit/<str:id>/',faq_edit, name='faq_edit'),
    path('faq-delete/<str:id>/',faq_delete, name='faq_delete'),

    #Counter
    path('counter-add/',counter_add, name='counter_add'),
    path('counter-view/',counter_view, name='counter_view'),
    path('counter-edit/<str:id>/',counter_edit, name='counter_edit'),
    path('counter-delete/<str:id>/',counter_delete, name='counter_delete'),

    #blog
    path('blog-add/',blog_add, name='blog_add'),
    path('blog-view/',blog_view, name='blog_view'),
    path('blog-edit/<str:id>/',blog_edit, name='blog_edit'),
    path('blog-delete/<str:id>/',blog_delete, name='blog_delete'),


    #service_service

    path('service-add/',service_add, name='service_add'),
    path('service-view/',service_view, name='service_view'),
    path('service-edit/<str:id>/',service_edit, name='service_edit'),
    path('service-delete/<str:id>/',service_delete, name='service_delete'),
]

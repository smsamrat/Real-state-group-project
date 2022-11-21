from django.urls import path
from .views import *

urlpatterns = [
    path('',dashboard, name='dashboard'),
    path('feedback-view/',feedback_view, name='feedback_view'),
    path('feedback-edit/<str:id>/',feedback_edit, name='feedback_edit'),
    path('feedback-approved/<str:id>/',feedback_approved, name='feedback_approved'),
    path('feedback-delete/<str:id>/',feedback_delete, name='feedback_delete'),

############# start related image inlineformset url ##############

    path('inline-form/',PropertyPostList.as_view(), name='PropertyPost-list'),
    path('PropertyPost/add/',PropertyPostRelatedImageCreate.as_view(), name='PropertyPost-add'),
    path('PropertyPost/update/<int:pk>',PropertyPostRelatedImageUpdate.as_view(), name='PropertyPost-update'),
    path('PropertyPost/details/view/<int:pk>',PropertyDetailsView.as_view(), name='PropertyPost-Details-view'),
    # path('PropertyPost/<int:pk>',PropertyPostDelete.as_view(), name='PropertyPost-delete'),
    path('property-delete/<str:id>/',property_delete, name='property_delete'),

############# end related image inlineformset url ##############

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

    #gallery_service

    path('gallery-add/',gallery_add, name='gallery_add'),
    path('gallery-view/',gallery_view, name='gallery_view'),
    path('gallery-edit/<str:id>/',gallery_edit, name='gallery_edit'),
    path('gallery-delete/<str:id>/',gallery_delete, name='gallery_delete'),

    #get in touch
        #career
    path('career-add/',career_add, name='career_add'),
    path('career-view/',career_view, name='career_view'),
    path('career-edit/<str:id>/',career_edit, name='career_edit'),
    path('career-delete/<str:id>/',career_delete, name='career_delete'),

    #job application
    path('job-application-view/',job_application_view, name='job_application_view'),
    path('job-application-edit/<str:id>/',job_application_edit, name='job_application_edit'),
    path('job-application-delete/<str:id>/',job_application_delete, name='job_application_delete'),

    #our team
    path('team-add/',team_add, name='team_add'),
    path('team-view/',team_view, name='team_view'),
    path('team-edit/<str:id>/',team_edit, name='team_edit'),
    path('team-delete/<str:id>/',team_delete, name='team_delete'),

    #our notice
    path('notice-add/',notice_add, name='notice_add'),
    path('notice-view/',notice_view, name='notice_view'),
    path('notice-edit/<str:id>/',notice_edit, name='notice_edit'),
    path('notice-delete/<str:id>/',notice_delete, name='notice_delete'),

    #Contact
    path('contact-view/',contact_view, name='contact_view'),
    path('contact-update/<str:id>/',contact_update, name='contact_update'),
    path('contact-delete/<str:id>/',contact_delete, name='contact_delete'),


    # About area
    # About head
    path('about-head-add/',about_head_add, name='about_head_add'),
    path('about-head-view/',about_head_view, name='about_head_view'),
    path('about-head-edit/<str:id>/',about_head_edit, name='about_head_edit'),
    path('about-head-delete/<str:id>/',about_head_delete, name='about_head_delete'),

    # About looking section

    path('about-looking-add/',about_looking_add, name='about_looking_add'),
    path('about-looking-view/',about_looking_view, name='about_looking_view'),
    path('about-looking-edit/<str:id>/',about_looking_edit, name='about_looking_edit'),
    path('about-looking-delete/<str:id>/',about_looking_delete, name='about_looking_delete'),

    # About looking section

    path('about-testimonial-add/',about_testimonial_add, name='about_testimonial_add'),
    path('about-testimonial-view/',about_testimonial_view, name='about_testimonial_view'),
    path('about-testimonial-edit/<str:id>/',about_testimonial_edit, name='about_testimonial_edit'),
    path('about-testimonial-delete/<str:id>/',about_testimonial_delete, name='about_testimonial_delete'),
]

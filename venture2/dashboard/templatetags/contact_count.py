from django import template
from indexApp.models import ContactUs,JobApplication,FeedBack
register = template.Library()

@register.filter
def contact_count(request):
    pending_contact= ContactUs.objects.filter(status='pending')
    return pending_contact.count()
    
@register.filter
def job_application_count(request):
    pending_job_application= JobApplication.objects.filter(status='pending')
    return pending_job_application.count()

@register.filter
def feedback_count(request):
    pending_feedback_count= FeedBack.objects.filter(status='pending')
    return pending_feedback_count.count()
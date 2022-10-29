from dataclasses import fields
from msilib.schema import Control
from django import forms 
from .models import ContactUs,JobApplication,FeedBack

class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your Name',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Your Email',
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your Phone',
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your Subject',
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Your Message',
        'rows': 4
    }))
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'phone', 'subject','message']


class JobApplicationForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Your Full Name',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Your Email',
    }))
    phone = forms.CharField(widget=forms.NumberInput(attrs={
        'class':'form-control',
        'maxlength': 15,
        'type': 'number',
        'placeholder':'Your Phone',
    }))

    expected_salary = forms.CharField(widget=forms.NumberInput(attrs={
        'class':'form-control',
        'type': 'number',
        'placeholder':'Expected salary',
    }))

    cv  = forms.FileField(label="Cardholder Name",widget=forms.ClearableFileInput(attrs={
        'class':'form-control',
        'placeholder':'Upload your cv',
        })
        )
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Your Message',
        'rows': 4
    }))
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'phone', 'expected_salary','cv','message']


class UserFeedbackForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control hidden',
        'placeholder':'Your Phone',
        
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Write a short descripton',
        'rows':3,
    }))

    class Meta:
        model = FeedBack
        fields =['name','description']
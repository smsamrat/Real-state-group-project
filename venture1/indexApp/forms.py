
from django import forms 
from .models import BookingPropertyType, ContactUs,JobApplication,FeedBack,BookingNow
from phonenumber_field.formfields import PhoneNumberField
# from phonenumber_field.widgets import PhoneNumberPrefixWidget
# from phonenumber_field.widgets import PhonePrefixSelect 

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
        'class':'form-control',
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


class BookingNowForm(forms.ModelForm):

    # PROPERTY_TYPE =[
    #     ('','Choose Property'),
    #     ('Apartment','Apartment'),
    #     ('Commercial','Commercial'),
    # ]

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
    }
    ))
    def clean(self):
        data  = self.cleaned_data.get('phone')


        # if str(data)==data:
        #     self._errors['phone'] = self.error_class([
        #         "Please Provide correct phone number in this field"
        #     ])

        if len(data)<10:
            self._errors['phone']=self.error_class([
                "At least 11 digit user in this field"
            ])

        if not data.isdigit():
            self._errors['phone']=self.error_class([
                "Please provide your valid phone number"
            ])

        return self.cleaned_data



    job_designation = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Designation',     
    }))


    property_type = forms.ModelChoiceField(queryset =BookingPropertyType.objects.all(),empty_label='Select Property', widget=forms.Select(attrs={
        'class':'form-select prt',
    }))

    property_size = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Property Size',
    }))

    roperty_description = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Write a short descripton',
        'rows':5,
    }))

    class Meta:
        model = BookingNow
        fields ='__all__'
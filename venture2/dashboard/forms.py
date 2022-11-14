from django import forms 
from django.forms import ModelForm
from indexApp.models import *
from ckeditor.widgets import CKEditorWidget

class PropertyPostForm(forms.ModelForm):
    class Meta:
        model = PropertyPost
        fields ='__all__'

class WhyChooseUsForm(forms.ModelForm):
    class Meta:
        model = Why_chosse_us
        fields ='__all__'

class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields ='__all__'

class CountersForm(forms.ModelForm):
    class Meta:
        model = Counters
        fields ='__all__'

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields ='__all__'

class ServicePostForm(forms.ModelForm):
    class Meta:
        model = ServicePost
        fields ='__all__'
        
class GalleryPostForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields ='__all__'


# class CareerAdmin(forms.ModelForm):
#     prepopulated_fields ={'slug': ('title',)}

class CareerForm(forms.ModelForm):
    # job_description = forms.CharField(widget=CKEditorWidget())

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',  
    }))

    post_date = forms.CharField(widget=forms.TextInput(attrs={
        'type':'date',  
    }))
    
    end_date = forms.CharField(widget=forms.TextInput(attrs={
        'type':'date', 
    }))

    class Meta:
        model = Career
        fields = ['title','job_description','post_date','end_date']

class OurTeamForm(forms.ModelForm):
    class Meta:
        model = OurTeam
        fields ='__all__'
        exclude = ['ordering']

class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields ='__all__'
from django import forms 
from indexApp.models import *

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

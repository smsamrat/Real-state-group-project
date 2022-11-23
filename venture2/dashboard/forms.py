from django import forms 
from django.forms import ModelForm
from indexApp.models import *
from dashboard.models import *
from ckeditor.widgets import CKEditorWidget



############ start related image inlineformset form ##########
from django.forms import ModelForm, inlineformset_factory


class PropertyPostForm(ModelForm):
    class Meta:
        model = PropertyPost
        exclude = ()


class RelatedImageForm(ModelForm):
    class Meta:
        model = Post_related_images
        exclude = ()


RelatedImageFormSet = inlineformset_factory(PropertyPost, Post_related_images,
                                            form=RelatedImageForm, extra=1)

############ end related image inlineformset form ##########

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

class AboutHeadForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields ='__all__'

class AboutLookingSectionForm(forms.ModelForm):
    class Meta:
        model = AboutLookingSection
        fields ='__all__'

class AboutTestimotialForm(forms.ModelForm):
    class Meta:
        model = AboutTestimotial
        fields ='__all__'

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'

class FeedBackApprovedForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
        exclude = ('status',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        # exclude = ('status',)

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = '__all__'
        # exclude = ('status',)

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
        # exclude = ('status',)


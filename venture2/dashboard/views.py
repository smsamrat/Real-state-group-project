from django.shortcuts import redirect, render
from .forms import *
from indexApp.models import *
from django.contrib import messages
from django.utils.text import slugify


############ start related image inlineformset functionality ##########
from django.db import transaction
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import RelatedImageFormSet
# from .models import PropertyPost

# Create your views here.

def dashboard(request):
    return render(request,'dashboard/index.html')



class PropertyPostList(ListView):
    model = PropertyPost
    template_name='dashboard/Postprofile/profile_list.html'


class PropertyPostCreate(CreateView):
    model = PropertyPost
    fields = '__all__'
    template_name='dashboard/Postprofile/profile_form.html'


class PropertyPostRelatedImageCreate(CreateView):
    model = PropertyPost
    fields = '__all__'
    template_name='dashboard/Postprofile/profile_form.html'
    success_url = reverse_lazy('PropertyPost-list')

    def get_context_data(self, **kwargs):
        data = super(PropertyPostRelatedImageCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['relatedimages'] = RelatedImageFormSet(self.request.POST,self.request.FILES)
        else:
            data['relatedimages'] = RelatedImageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        relatedimages = context['relatedimages']
        with transaction.atomic():
            self.object = form.save()

            if relatedimages.is_valid():
                relatedimages.instance = self.object
                relatedimages.save()
        return super(PropertyPostRelatedImageCreate, self).form_valid(form)


class PropertyPostUpdate(UpdateView):
    model = PropertyPost
    success_url = '/'
    fields = '__all__'
    template_name='dashboard/Postprofile/profile_form.html'


class PropertyPostRelatedImageUpdate(UpdateView):
    model = PropertyPost
    fields = '__all__'
    template_name='dashboard/Postprofile/profile_form.html'
    success_url = reverse_lazy('PropertyPost-list')

    def get_context_data(self, **kwargs):
        data = super(PropertyPostRelatedImageUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['relatedimages'] = RelatedImageFormSet(self.request.POST,self.request.FILES, instance=self.object)
        else:
            data['relatedimages'] = RelatedImageFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        relatedimages = context['relatedimages']
        with transaction.atomic():
            self.object = form.save()
            if relatedimages.is_valid():
                relatedimages.instance = self.object
                relatedimages.save()
        return super(PropertyPostRelatedImageUpdate, self).form_valid(form)



class PropertyDetailsView(UpdateView):
    model = PropertyPost
    fields = '__all__'
    template_name='dashboard/Postprofile/property-details-view.html'
    success_url = reverse_lazy('PropertyPost-list')

    def get_context_data(self, **kwargs):
        data = super(PropertyDetailsView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['relatedimages'] = RelatedImageFormSet(self.request.POST,self.request.FILES, instance=self.object)
        else:
            data['relatedimages'] = RelatedImageFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        relatedimages = context['relatedimages']
        with transaction.atomic():
            self.object = form.save()
            if relatedimages.is_valid():
                relatedimages.instance = self.object
                relatedimages.save()
        return super(PropertyDetailsView, self).form_valid(form)




# class PropertyPostDelete(DeleteView):
#     model = PropertyPost
#     success_url = reverse_lazy('PropertyPost-list')



def property_delete(request,id):
    property_views = PropertyPost.objects.get(id=id)
    property_views.delete()
    messages.success(request,'Delete Successfully')
    return redirect('PropertyPost-list')


############ end related image inlineformset functionality ##########


#why_chosse_us

def why_choose_us_add(request):
    form = WhyChooseUsForm()
    if request.method=='POST':
        form = WhyChooseUsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('why_choose_us_view')
        else:
            form = WhyChooseUsForm()
            return render(request, 'dashboard/why_choose_us/why_choose_us_add.html',{'form':form})
    return render(request,'dashboard/why_choose_us/why_choose_us_add.html',{'form':form})

def why_choose_us_view(request):
    query = Why_chosse_us.objects.all()
    return render(request,'dashboard/why_choose_us/why_choose_us_view.html',{'query':query})

def why_choose_us_edit(request,id):
    query = Why_chosse_us.objects.get(id=id)
    form = WhyChooseUsForm(instance =query)
    if request.method=='POST':

        form = WhyChooseUsForm(request.POST,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('why_choose_us_view')
        else:
            form = WhyChooseUsForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/why_choose_us/why_choose_us_edit.html',{'form':form})

    return render(request,'dashboard/why_choose_us/why_choose_us_edit.html',{'form':form})

def why_choose_us_delete(request,id):
    query = Why_chosse_us.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('why_choose_us_view')



#Faq functionality

def faq_add(request):
    form = FaqForm()
    if request.method=='POST':
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('faq_view')
        else:
            form = FaqForm()
            return render(request, 'dashboard/faq/faq_add.html',{'form':form})
    return render(request,'dashboard/faq/faq_add.html',{'form':form})

def faq_view(request):
    query = Faq.objects.all()
    return render(request,'dashboard/faq/faq_view.html',{'query':query})

def faq_edit(request,id):
    query = Faq.objects.get(id=id)
    form = FaqForm(instance =query)
    if request.method=='POST':

        form = FaqForm(request.POST,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('faq_view')
        else:
            form = FaqForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/faq/faq_edit.html',{'form':form})

    return render(request,'dashboard/faq/faq_edit.html',{'form':form})

def faq_delete(request,id):
    query = Faq.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('faq_view')


#Counter functionality

def counter_add(request):
    form = CountersForm()
    if request.method=='POST':
        form = CountersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('counter_view')
        else:
            form = FaqForm()
            return render(request, 'dashboard/counter/counter_add.html',{'form':form})
    return render(request,'dashboard/counter/counter_add.html',{'form':form})

def counter_view(request):
    query = Counters.objects.all()
    return render(request,'dashboard/counter/counter_view.html',{'query':query})

def counter_edit(request,id):
    query = Counters.objects.get(id=id)
    form = CountersForm(instance =query)
    if request.method=='POST':

        form = CountersForm(request.POST,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('counter_view')
        else:
            form = CountersForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/counter/counter_edit.html',{'form':form})

    return render(request,'dashboard/counter/counter_edit.html',{'form':form})

def counter_delete(request,id):
    query = Counters.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('counter_view')


#Blog functionality

def blog_add(request):
    form = BlogForm()
    if request.method=='POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('blog_view')
        else:
            form = BlogForm(request.POST)
            return render(request, 'dashboard/blog/blog_add.html',{'form':form})
    return render(request,'dashboard/blog/blog_add.html',{'form':form})

def blog_view(request):
    query = blog.objects.all()
    return render(request,'dashboard/blog/blog_view.html',{'query':query})

def blog_edit(request,id):
    query = blog.objects.get(id=id)
    form = BlogForm(instance =query)
    if request.method=='POST':

        form = BlogForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('blog_view')
        else:
            form = BlogForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/blog/blog_edit.html',{'form':form})

    return render(request,'dashboard/blog/blog_edit.html',{'form':form})

def blog_delete(request,id):
    query = blog.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('blog_view')

#Service functionality

def service_add(request):
    form = ServicePostForm()
    if request.method=='POST':
        form = ServicePostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('service_view')
        else:
            form = ServicePostForm(request.POST)
            return render(request, 'dashboard/service/service_add.html',{'form':form})
    return render(request,'dashboard/service/service_add.html',{'form':form})

def service_view(request):
    query = ServicePost.objects.all()
    return render(request,'dashboard/service/service_view.html',{'query':query})

def service_edit(request,id):
    query = ServicePost.objects.get(id=id)
    form = ServicePostForm(instance =query)
    if request.method=='POST':

        form = ServicePostForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('service_view')
        else:
            form = ServicePostForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/service/service_edit.html',{'form':form})

    return render(request,'dashboard/service/service_edit.html',{'form':form})

def service_delete(request,id):
    query = ServicePost.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('service_view')


#Gallery functionality

def gallery_add(request):
    form = GalleryPostForm()
    if request.method=='POST':
        form = GalleryPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('gallery_view')
        else:
            form = GalleryPostForm(request.POST)
            return render(request, 'dashboard/gallery/gallery_add.html',{'form':form})
    return render(request,'dashboard/gallery/gallery_add.html',{'form':form})

def gallery_view(request):
    query = Gallery.objects.all()
    return render(request,'dashboard/gallery/gallery_view.html',{'query':query})

def gallery_edit(request,id):
    query = Gallery.objects.get(id=id)
    form = GalleryPostForm(instance =query)
    if request.method=='POST':

        form = GalleryPostForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('gallery_view')
        else:
            form = GalleryPostForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/gallery/gallery_edit.html',{'form':form})

    return render(request,'dashboard/gallery/gallery_edit.html',{'form':form})

def gallery_delete(request,id):
    query = Gallery.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('gallery_view')


#get in touch functionality

def career_add(request):
    form = CareerForm()
    if request.method=='POST':
        form = CareerForm(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            #assign the current slug and user to the post
            # new_post.title = request.user
            new_post.slug = slugify(new_post.title)
            #save post to database
            new_post.save()
            messages.success(request,'Successfully Submit')
            return redirect('career_view')
        else:
            form = CareerForm(request.POST)
            return render(request, 'dashboard/get_in_touch/career_add.html',{'form':form})
    return render(request,'dashboard/get_in_touch/career_add.html',{'form':form})

def career_view(request):
    query = Career.objects.all()
    return render(request,'dashboard/get_in_touch/career_view.html',{'query':query})

def career_edit(request,id):
    query = Career.objects.get(id=id)
    form = CareerForm(instance =query)
    if request.method=='POST':

        form = CareerForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('career_view')
        else:
            form = GalleryPostForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/get_in_touch/career_edit.html',{'form':form})

    return render(request,'dashboard/get_in_touch/career_edit.html',{'form':form})

def career_delete(request,id):
    query = Career.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('career_view')

    #Job Application 

def job_application_view(request):
    query = JobApplication.objects.all()
    return render(request,'dashboard/get_in_touch/job_application_view.html',{'query':query})

def  job_application_delete(request,id):
    query = JobApplication.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('job_application_view')
    


    #Our team functionality

def team_add(request):
    form = OurTeamForm()
    if request.method=='POST':
        form = OurTeamForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('team_view')
        else:
            form = OurTeamForm(request.POST)
            return render(request, 'dashboard/get_in_touch/team/team_add.html',{'form':form})
    return render(request,'dashboard/get_in_touch/team/team_add.html',{'form':form})

def team_view(request):
    query = OurTeam.objects.all()
    return render(request,'dashboard/get_in_touch/team/team_view.html',{'query':query})

def team_edit(request,id):
    query = OurTeam.objects.get(id=id)
    form = OurTeamForm(instance =query)
    if request.method=='POST':

        form = OurTeamForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('team_view')
        else:
            form = OurTeamForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/get_in_touch/team/team_edit.html',{'form':form})

    return render(request,'dashboard/get_in_touch/team/team_edit.html',{'form':form})

def team_delete(request,id):
    query = OurTeam.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('team_view')


    #Notice functionality

def notice_add(request):
    form = NoticeForm()
    if request.method=='POST':
        form = NoticeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('notice_view')
        else:
            form = NoticeForm(request.POST)
            return render(request, 'dashboard/get_in_touch/notice/notice_add.html',{'form':form})
    return render(request,'dashboard/get_in_touch/notice/notice_add.html',{'form':form})

def notice_view(request):
    query = Notice.objects.all()
    return render(request,'dashboard/get_in_touch/notice/notice_view.html',{'query':query})

def notice_edit(request,id):
    query = Notice.objects.get(id=id)
    form = NoticeForm(instance =query)
    if request.method=='POST':

        form = NoticeForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('notice_view')
        else:
            form = NoticeForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/get_in_touch/notice/notice_edit.html',{'form':form})

    return render(request,'dashboard/get_in_touch/notice/notice_edit.html',{'form':form})

def notice_delete(request,id):
    query = Notice.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('notice_view')

#contact funtionality

def contact_view(request):
    query = ContactUs.objects.all()
    return render(request,'dashboard/get_in_touch/contact_view.html',{'query':query})

def contact_delete(request,id):
    query = ContactUs.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('contact_view')


# About Area

def about_head_add(request):
    form = AboutHeadForm()
    if request.method=='POST':
        form = AboutHeadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('about_head_view')
        else:
            form = AboutHeadForm(request.POST)
            return render(request, 'dashboard/about/about_head_section/about_head_add.html',{'form':form})
    return render(request,'dashboard/about/about_head_section/about_head_add.html',{'form':form})

def about_head_view(request):
    query = AboutUs.objects.all()
    return render(request,'dashboard/about/about_head_section/about_head_view.html',{'query':query})

def about_head_edit(request,id):
    query = AboutUs.objects.get(id=id)
    form = AboutHeadForm(instance =query)
    if request.method=='POST':

        form = AboutHeadForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('about_head_view')
        else:
            form = AboutHeadForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/about/about_head_section/about_head_edit.html',{'form':form})

    return render(request,'dashboard/about/about_head_section/about_head_edit.html',{'form':form})

def about_head_delete(request,id):
    query = AboutUs.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('about_head_view')

    #about looking section

def about_looking_add(request):
    form = AboutLookingSectionForm()
    if request.method=='POST':
        form = AboutLookingSectionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('about_looking_view')
        else:
            form = AboutHeadForm(request.POST)
            return render(request, 'dashboard/about/about_looking_section/about_looking_add.html',{'form':form})
    return render(request,'dashboard/about/about_looking_section/about_looking_add.html',{'form':form})

def about_looking_view(request):
    query = AboutLookingSection.objects.all()
    return render(request,'dashboard/about/about_looking_section/about_looking_view.html',{'query':query})

def about_looking_edit(request,id):
    query = AboutLookingSection.objects.get(id=id)
    form = AboutLookingSectionForm(instance =query)
    if request.method=='POST':

        form = AboutLookingSectionForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('about_looking_view')
        else:
            form = AboutLookingSectionForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/about/about_looking_section/about_looking_edit.html',{'form':form})

    return render(request,'dashboard/about/about_looking_section/about_looking_edit.html',{'form':form})

def about_looking_delete(request,id):
    query = AboutLookingSection.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('about_looking_view')

#about testimonial section

def about_testimonial_add(request):
    form = AboutTestimotialForm()
    if request.method=='POST':
        form = AboutTestimotialForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('about_testimonial_view')
        else:
            form = AboutTestimotialForm(request.POST)
            return render(request, 'dashboard/about/about_testimonial_section/about_testimonial_add.html',{'form':form})
    return render(request,'dashboard/about/about_testimonial_section/about_testimonial_add.html',{'form':form})

def about_testimonial_view(request):
    query = AboutTestimotial.objects.all()
    return render(request,'dashboard/about/about_testimonial_section/about_testimonial_view.html',{'query':query})

def about_testimonial_edit(request,id):
    query = AboutTestimotial.objects.get(id=id)
    form = AboutTestimotialForm(instance =query)
    if request.method=='POST':

        form = AboutTestimotialForm(request.POST,request.FILES,instance=query)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('about_testimonial_view')
        else:
            form = AboutTestimotialForm(instance =query)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/about/about_testimonial_section/about_testimonial_edit.html',{'form':form})

    return render(request,'dashboard/about/about_testimonial_section/about_testimonial_edit.html',{'form':form})

def about_testimonial_delete(request,id):
    query = AboutTestimotial.objects.get(id=id)
    query.delete()
    messages.success(request,'Delete Successfully')
    return redirect('about_testimonial_view')
    

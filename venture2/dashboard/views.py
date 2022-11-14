from django.shortcuts import redirect, render
from .forms import *
from indexApp.models import *
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.
def dashboard(request):
    return render(request,'dashboard/index.html')


def property_add(request):
    form = PropertyPostForm(request.POST)
    if request.method=='POST':
        form = PropertyPostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Post')
            return redirect('property_view')
        else:
            form = PropertyPostForm()
            return render(request, 'dashboard/property_file/property_post.html',{'form':form})
    context = {
        'form':form
    }
    return render(request,'dashboard/property_file/property_post.html',context)


def property_view(request):
    property_views = PropertyPost.objects.all()
    context = {
        'property_views':property_views
    }
    return render(request,'dashboard/property_file/property_view.html',context)

def property_edit(request,id):
    property_edit_q = PropertyPost.objects.get(id=id)
    form = PropertyPostForm(instance =property_edit_q)
    if request.method=='POST':

        form = PropertyPostForm(request.POST,request.FILES,instance=property_edit_q)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Update')
            return redirect('property_view')
        else:
            form = PropertyPostForm(instance =property_edit_q)
            messages.success(request,'Successfully not Update')
            return render(request, 'dashboard/property_file/property_edit.html',{'form':form})
    context = {
        'form':form
    }
    return render(request,'dashboard/property_file/property_edit.html',context)

def property_delete(request,id):
    property_views = PropertyPost.objects.get(id=id)
    property_views.delete()
    messages.success(request,'Delete Successfully')
    return redirect('property_view')
    return render(request,'dashboard/property_file/property_view.html')


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
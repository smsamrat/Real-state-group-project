from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

def Home(request):
    banner_query = Baner_video.objects.all()
    location_query = Location.objects.filter()
    location_filter= request.GET.get('location')
    if location_filter:
        feature_query = PropertyPost.objects.filter(post_location__location_name = location_filter)
        paginator = Paginator(feature_query,10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
    else:
        feature_query = PropertyPost.objects.filter(post_type__name='Feature Property')
        paginator = Paginator(feature_query,10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    recent_query = PropertyPost.objects.filter(post_type__name='Recent Property')
    paginator = Paginator(recent_query,12)
    page_number = request.GET.get('page', 1)
    recent_query_obj = paginator.get_page(page_number)

    why_chosse_us_q = Why_chosse_us.objects.all()
    counters = Counters.objects.all()
    agent_query = Agent.objects.all()
    blog_query = blog.objects.all()
    faq_query = Faq.objects.all()
    context ={
        'banner_details':banner_query,
        'feature_details':page_obj,
        'page_number':int(page_number),
        'paginator':paginator,
        'counters_details':counters,
        'location_details':location_query,
        'agent_details':agent_query,
        'recent_property':recent_query_obj,
        'blog_querys':blog_query,
        'why_chosse_us_q':why_chosse_us_q,
        'faq_query':faq_query,
    }
    return render(request,'index.html',context)


def land_project(request):
    feature_query = PropertyPost.objects.filter(post_type__name='Land Property')
    paginator = Paginator(feature_query,9,orphans=1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context ={
        'feature_details':page_obj,
        'page_number':int(page_number),
        'paginator':paginator,
    }
    return render(request,'property/land_project.html',context)

def apartment_project(request):
    feature_query = PropertyPost.objects.filter(post_type__name='Apartment Property')
    paginator = Paginator(feature_query,9,orphans=1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)

    division = Division.objects.all()
    dis_name = request.GET.get('dis')
    city = District.objects.filter()

    project_type_filters = ProjectTypeFilter.objects.all()
    context ={
        'feature_details':page_obj,
        'page_number':int(page_number),
        'paginator':paginator,
        'divisions':division,
        'cities':city, 
        'project_type_filters':project_type_filters, 
    }
    return render(request,'property/apartment_project.html',context)

def apartment_details_property(request,id):
    single_post = PropertyPost.objects.get(id=id)
    related_images = Post_related_images.objects.filter(post=single_post)

    form = UserFeedbackForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.property_id = single_post.id
            form.save()
            messages.success(request,'Successfully Submitted')
            return redirect('details_property',id=id)
        else:
            form = ContactForm(request.POST)
            messages.error(request,'Message Not Submitted')
            return redirect('details_property',id=id)
           
    context= {
        'apartment_details':single_post,
        'related_images':related_images,
        'form': form
    }


    return render(request,'property_details/apartment_details.html',context)

def feature_details_property(request,id):
    single_post = PropertyPost.objects.get(id=id)
    related_images = Post_related_images.objects.filter(post=single_post)

    form = UserFeedbackForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submitted')
            return redirect('feature_details_property',id=id)
        else:
            form = ContactForm(request.POST)
            messages.error(request,'Message Not Submitted')
            return redirect('feature_details_property',id=id)
    context= {
        'feature_property_details':single_post,
        'related_images':related_images,
        'form':form,
    }

    return render(request,'property_details/feature_details_property.html',context)
    
def recent_details_property(request,id):
    single_post = PropertyPost.objects.get(id=id)
    related_images = Post_related_images.objects.filter(post=single_post)

    form = UserFeedbackForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submitted')
            return redirect('recent_details_property',id=id)
        else:
            form = ContactForm(request.POST)
            messages.error(request,'Message Not Submitted')
            return redirect('recent_details_property',id=id)
    context= {
        'recent_property_details':single_post,
        'related_images':related_images,
        'form':form,
        
    }

    return render(request,'property_details/recent_details_property.html',context)

def land_details_property(request,id):
    single_post = PropertyPost.objects.get(id=id)
    related_images = Post_related_images.objects.filter(post=single_post)

    form = UserFeedbackForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submitted')
            return redirect('land_details_property',id=id)
        else:
            form = ContactForm(request.POST)
            messages.error(request,'Message Not Submitted')
            return redirect('land_details_property',id=id)
    context= {
        'land_details':single_post,
        'related_images':related_images,
        'form':form
    }

    return render(request,'property_details/land_details_property.html',context)


def venture_trending(request):
    venture_trending_q = ServicePost.objects.filter(service_type__name='Venture Trending')
    context ={
        'venture_trending_q':venture_trending_q
    }
    return render(request,'service/Venture Trending.html',context)

def Venture_Security(request):
    Venture_Security_q = ServicePost.objects.filter(service_type__name='Venture Security')
    context ={
    'Venture_Security_q':Venture_Security_q
    }
    return render(request,'service/Venture Security.html',context)

def Venture_design_Development(request):
    Venture_design_Development_q = ServicePost.objects.filter(service_type__name='Venture Design & Development')
    context ={
        'Venture_design_Development_q':Venture_design_Development_q
    }
    return render(request,'service/Venture Design Development .html',context)

def Venture_it(request):
    Venture_it_q = ServicePost.objects.filter(service_type__name='Venture IT')
    context ={
        'Venture_it_q':Venture_it_q
    }
    return render(request,'service/Venture IT.html',context)
    
def Venture_tourism(request):
    Venture_tourism_q = ServicePost.objects.filter(service_type__name='Venture Tourism & Hospital')
    context ={
        'Venture_tourism_q':Venture_tourism_q
    }
    return render(request,'service/Venture Tourism & Hospital.html',context)

def service_details(request,id):
    service_detail_q = ServicePost.objects.get(id=id)
    related_images = Service_related_images.objects.filter(service=service_detail_q)
    context= {
        'service_detail_q':service_detail_q,
        'related_images':related_images,
    }
    return render(request,'service/service_details.html',context)

def blogs(request):
    blog_query = blog.objects.all()
    context= {
        'blog_query':blog_query
    }
    return render(request,'blog/blog.html',context)

def readMore(request,id):
    single_blog = blog.objects.get(id=id)
    context= {
        'single_blog':single_blog
    }
    return render(request,'blog/read_More.html',context)

def about(request):
    about_query = AboutUs.objects.all()
    LookingSection = AboutLookingSection.objects.all()
    about_estimotial = AboutTestimotial.objects.all()
    context = {
        'about_query' : about_query,
        'LookingSections' : LookingSection,
        'about_testimotial' : about_estimotial,
    }
    return render(request,'about/about.html',context)

def gallay(request):
    gallery_office = Gallery.objects.all()
    # gallery_client = Gallery.objects.filter(img_type = 'Client')
    # gallery_project = Gallery.objects.filter(img_type = 'Project')
    context = {
        'gallery_office':gallery_office,
        # 'gallery_client':gallery_client,
        # 'gallery_project':gallery_project,
    }
    return render(request,'gallery/office.html',context)

def video(request):
    return render(request,'gallery/video.html')



def our_team(request):
    team_profile = OurTeam.objects.all()

    context={
        'team_profile':team_profile
    }
    return render(request, 'get_in_touch/our_team.html',context)

def contact(request):
    form = ContactForm(request.POST)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('contactus')
        else:
            form = ContactForm(request.POST)
            return render(request, 'get_in_touch/contact.html',{'form':form})
    return render(request, 'get_in_touch/contact.html',{'form':form})


def career(request):
    career = Career.objects.all()
    context ={
        'career':career
    }
    return render(request, 'get_in_touch/career.html',context)

def career_detail(request,slug):
    careers = Career.objects.get(slug=slug)
    form = JobApplicationForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('career-detail', slug=slug)
        else:
            form = JobApplicationForm()
            return render(request, 'get_in_touch/career-details.html',{'form':form})

    context={
        'careers':careers,
        'form':form
    }
    return render(request, 'get_in_touch/career-details.html',context)

def notice(request):
    notice = Notice.objects.all()
    return render(request, 'get_in_touch/notice.html', {'notice':notice})

def location(request,location_name):
    if location_name:
        location_query = PropertyPost.objects.filter(post_location__location_name = location_name)

        context ={
            'feature_details':location_query
        }

    return render(request,'location_wise_post.html',context)

def booking_now(request):
    form = BookingNowForm()
    if request.method == 'POST':
        form = BookingNowForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Submit')
            return redirect('booking_now')

    context = {
        'form':form
    }
    return render(request,'booking_now.html',context)

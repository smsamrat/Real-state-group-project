from django.shortcuts import redirect, render
from indexApp.forms import JobApplicationForm,ContactForm
from .models import *
from django.core.paginator import Paginator
from django.contrib import messages
# Create your views here.

def Home(request):
    banner_query = Baner_video.objects.all()
    location_query = Location.objects.filter()
    location_filter= request.GET.get('location')
    if location_filter:
        feature_query = Post.objects.filter(post_location__location_name = location_filter)
        paginator = Paginator(feature_query,10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
    else:
        feature_query = Post.objects.filter(post_type='feature')
        paginator = Paginator(feature_query,10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    recent_query = Post.objects.filter(post_type='recent')
    paginator = Paginator(recent_query,12)
    page_number = request.GET.get('page', 1)
    recent_query_obj = paginator.get_page(page_number)

    counters = Counters.objects.all()
    agent_query = Agent.objects.all()
    blog_query = blog.objects.all()
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
    }
    return render(request,'index.html',context)


def land_project(request):
    feature_query = Post.objects.filter(post_type='land')
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
    feature_query = Post.objects.filter(post_type='apartment')
    paginator = Paginator(feature_query,9,orphans=1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    print(page_obj)

    division = Division.objects.all()
    dis_name = request.GET.get('dis')
    city = District.objects.filter()

    context ={
        'feature_details':page_obj,
        'page_number':int(page_number),
        'paginator':paginator,
        'divisions':division,
        'cities':city,
    }
    return render(request,'property/apartment_project.html',context)

def apartment_details_property(request,id):
    single_post = Post.objects.get(id=id)
    related_images = Post_related_images.objects.filter(post=single_post)
    context= {
        'apartment_details':single_post,
        'related_images':related_images
    }

    return render(request,'property_details/apartment_details.html',context)

def feature_details_property(request,id):
    single_post = Post.objects.get(id=id)
    context= {
        'single_post':single_post
    }

    return render(request,'property_details/feature_details_property.html',context)
    
def recent_details_property(request,id):
    single_post = Post.objects.get(id=id)
    context= {
        'single_post':single_post
    }

    return render(request,'property_details/recent_details_property.html',context)

def land_details_property(request,id):
    single_post = Post.objects.get(id=id)
    context= {
        'single_post':single_post
    }

    return render(request,'property_details/land_details_property.html',context)


def service(request):
    return render(request,'service/service.html')

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
    agent_query = Agent.objects.all()
    context = {
        'agent_details':agent_query
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
        location_query = Post.objects.filter(post_location__location_name = location_name)

        context ={
            'feature_details':location_query
        }

    return render(request,'location_wise_post.html',context)
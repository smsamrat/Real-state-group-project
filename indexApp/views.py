from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def Home(request):
    banner_query = Baner_video.objects.all()
    location_query = Location.objects.filter()
    location_filter= request.GET.get('location')
    if location_filter:
        feature_query = Features_property_post.objects.filter(post_location__location_name = location_filter)
        paginator = Paginator(feature_query,10)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
    else:
        feature_query = Features_property_post.objects.all()
        paginator = Paginator(feature_query,2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    recent_pro_query = Recently_Properties.objects.all()
    counters = Counters.objects.all()
    agent_query = Agent.objects.all()
    context ={
        'banner_details':banner_query,
        'feature_details':page_obj,
        'page_number':int(page_number),
        'paginator':paginator,
        'recent_pro_details':recent_pro_query,
        'counters_details':counters,
        'location_details':location_query,
        'agent_details':agent_query,
    }
    return render(request,'index.html',context)


def land_project(request):
    return render(request,'property/land_project.html')

def apartment_project(request):
    feature_query = Features_property_post.objects.all()
    paginator = Paginator(feature_query,6,orphans=1)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context ={
        'feature_details':page_obj,
        'page_number':int(page_number),
        'paginator':paginator,
    }
    return render(request,'property/apartment_project.html',context)

def service(request):
    return render(request,'service/service.html')

def blog(request):
    return render(request,'blog/blog.html')

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
    print(gallery_office)
    context = {
        'gallery_office':gallery_office,
        # 'gallery_client':gallery_client,
        # 'gallery_project':gallery_project,
    }
    return render(request,'gallery/office.html',context)

from django.shortcuts import redirect, render
from .forms import *
from indexApp.models import *
from django.contrib import messages

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



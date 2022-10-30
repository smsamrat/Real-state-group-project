from pydoc import describe
from random import choice
from tabnanny import verbose
from django.utils import timezone
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='children')

    def __str__(self):
        return self.name

class Baner_video(models.Model):
    video_link = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    title1 = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.title}"
class Location(models.Model):
    location_name = models.CharField(max_length=250)
    location_pic= models.ImageField(upload_to="location_img/",null=True)
    def __str__(self):
        return f'{self.location_name}'

class Property_type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class PropertyPost(models.Model):
    LIFT=(
        ('Yes','Yes'),
        ('No','No'),
    )
    post_pic = models.ImageField(upload_to='features_post_img/',blank=True,null=True)
    price = models.FloatField(default='0.00')
    post_title = models.CharField(max_length=250,blank=True,null=True)
    post_location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='location',blank=True,null=True)
    post_type = models.ManyToManyField(Property_type, related_name='pro_type',blank=True)
    land_size = models.IntegerField(blank=True,null=True)
    bedrooms = models.IntegerField(blank=True,null=True)
    bathrooms = models.IntegerField(blank=True,null=True)
    apartment_size = models.IntegerField(blank=True,null=True)
    total_apartment = models.IntegerField(blank=True,null=True)
    parking_area = models.CharField(max_length=100,blank=True,null=True)
    parking_size = models.IntegerField(blank=True,null=True)
    facing = models.CharField(max_length=100,blank=True,null=True)
    lift = models.CharField(max_length=100,choices=LIFT,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    floor_plan_image_or_land_layout_img = models.ImageField(upload_to='floor_plan_image/',blank=True, null=True)
    developer_name = models.CharField(max_length=250,blank=True, null=True)
    created_date =models.DateTimeField(auto_now_add=True)

    def get_date(self):
        return self.created_date.date()

    def __str__(self):
        return f'{self.post_title}{self.post_pic.url}'

    class Meta:
        ordering= ['-created_date']

class Post_related_images(models.Model):
    post = models.ForeignKey(PropertyPost, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Post_related_images')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.post_title

class Recently_Properties(models.Model):
    images = models.ImageField(upload_to='Recently_Properties/')
    for_rent = models.CharField(max_length=250,blank=True, null=True)
    for_sale = models.CharField(max_length=250,blank=True, null=True)
    price = models.FloatField(default='0.00',blank=True, null=True)
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    sqr_feet = models.CharField(max_length=250)
    bedrooms = models.CharField(max_length=250)
    bathrooms = models.CharField(max_length=250)
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        ordering=['-created']

class Counters(models.Model):
    counter_for_sale = models.IntegerField(default='0')
    counter_for_rent = models.IntegerField(default='0')
    brokers = models.IntegerField(default='0')
    agents = models.IntegerField(default='0')

    def __str__(self):
        return f"Num_of_Counters: {self.counter_for_rent}"

class Agent(models.Model):
    images = models.ImageField(upload_to='Agent_img/')
    name = models.CharField(max_length=250)
    disignation = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=250,null=True)
    mobile = models.CharField(max_length=250)
    fax = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

 
    def __str__(self):
        return f"{self.option_name}"
    class Meta:
        verbose_name = 'Why_chosse_us_option'
        verbose_name_plural = 'Why_chosse_us_options'


class Why_chosse_us(models.Model):
    title = models.CharField(max_length=100,null=True)
    description = models.TextField()
     
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = 'Why_chosse_us'
        verbose_name_plural = 'Why_chosse_us'

class Gallery(models.Model):
    IMG_TYPE = (
        ('Management','Management'),
        ('Realstate Property','Realstate Property'),
        ('E-commerce','E-commerce'),
        ('Client Area','Client Area')
    )   
    img = models.ImageField(upload_to='gallery/office/',blank=True,null=True)
    img_type = models.CharField(max_length=100, choices=IMG_TYPE, blank=True, null=True)

    def __str__(self):
        return f"Image type: {self.img_type}/{self.img}"


class Division(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class District(models.Model):
    country = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Area(models.Model):
    city = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class blog(models.Model):
    blog_img = models.ImageField(upload_to="blog_images")
    title = models.CharField(max_length=250)
    details = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_date(self):
        return self.created.date()

    def get_month(self):
        return self.created.strftime("%B")


class AboutUs(models.Model):
    main_image =  models.ImageField(upload_to='about-us_img/')
    shadow_image = models.ImageField(upload_to='about-us_img/')
    experience_year = models.IntegerField()
    title = models.CharField(max_length=150,null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.experience_year} of year experience'

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'About Us'

class AboutLookingSection(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'AboutLookingSection'
        verbose_name_plural = 'About looking section'

class AboutTestimotial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    short_description = models.TextField()
    image =  models.ImageField(upload_to='about-us_img/')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'AboutTestimotial'
        verbose_name_plural = 'About Testimotial'


class OurTeam(models.Model):
    name  = models.CharField(max_length = 150)
    designation = models.CharField(max_length = 150)
    image  = models.ImageField(upload_to='TeamImage')
    cover_image  = models.ImageField(upload_to='TeamImage')
    facebook_link = models.URLField(max_length = 500, blank=True,null=True)
    twitter_link = models.URLField(max_length = 500,blank=True,null=True)
    linkedin_link = models.URLField(max_length = 500,blank=True,null=True)
    instagram_link = models.URLField(max_length = 500,blank=True,null=True)
    ordering  = models.IntegerField(blank=True,null=True)
    
    class Meta:
        ordering =['ordering']
        verbose_name = 'OurTeam'
        verbose_name_plural = 'OurTeam'

    def __str__(self):
        return self.name

class Career(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50)
    active_status = models.BooleanField(default=True)
    job_description =RichTextUploadingField()
    post_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class Notice(models.Model):
    title  = models.CharField(max_length = 150)
    notice_file  = models.FileField(upload_to='Notice')
    
    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title

class ContactUs(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    phone = models.CharField(max_length = 150)
    subject = models.CharField(max_length = 150)
    message  = models.TextField()
    
    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'

    def __str__(self):
        return self.email

class JobApplication(models.Model):
    full_name= models.CharField(max_length = 150)
    email = models.EmailField()
    phone= models.CharField(max_length = 150)
    expected_salary= models.CharField(max_length = 150)
    cv= models.FileField(upload_to='ApplicationCV')
    message = models.TextField()
    
    def __str__(self):
        return self.email

class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    property_id = models.IntegerField(blank=True,null=True)
    description = models.TextField()
    is_feedback_show = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name



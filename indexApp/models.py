from email.policy import default
from random import choices
from secrets import choice
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models

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


class Post(models.Model):
    POST_TYPE=(
        ('feature','feature'),
        ('apartment','apartment'),
        ('land','land'),
        ('recent','recent'),
    )
    post_pic = models.ImageField(upload_to='features_post_img/',null=True)
    price = models.FloatField(default='0.00')
    post_title = models.CharField(max_length=250,null=True)
    post_location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='location',blank=True,null=True)
    post_type = models.CharField(max_length=100,choices=POST_TYPE)
    sqr_feet = models.CharField(max_length=250)
    bedrooms = models.CharField(max_length=250)
    bathrooms = models.CharField(max_length=250)
    garage = models.CharField(max_length=250)
    developer_name = models.CharField(max_length=250,blank=True, null=True)
    created_date =models.DateTimeField(auto_now_add=True)

    def get_date(self):
        return self.created_date.date()

    def __str__(self):
        return f'{self.post_title}{self.post_pic.url}'

    class Meta:
        ordering= ['-created_date']


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

class Gallery(models.Model):
    IMG_TYPE = (
        ('Office','Office'),
        ('Client','Client'),
        ('Project','Project'),
    )
    img = models.ImageField(upload_to='gallery/office/',blank=True,null=True)
    img_type = models.CharField(max_length=100, choices=IMG_TYPE, blank=True, null=True)

    def __str__(self):
        return f"Image type: {self.img_type}/{self.img}"

# class blog(models.Model):
#     blog_img = models.ImageField(upload_to="blog_images")
#     title = models.CharField(max_length=250)
#     details = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
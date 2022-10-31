from distutils.command.upload import upload
from statistics import mode
from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='images/')

class Category(models.Model):
    name = models.CharField(max_length=20)

class Product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Post(models.Model):
    GENDER_CHOICES  = (('male','male'),('female','female'),)
    username = models.CharField(max_length=100,null=False,blank=False)
    text = models.TextField(null=False,blank=False)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default='male')
    time = models.DateTimeField(auto_now_add=True)





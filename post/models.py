from django.db import models

from django.urls import reverse
from datetime import datetime, date, time
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
            return reverse('home')
class post(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')
    authour = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    post_time = models.TimeField(auto_now_add=True)
    category = models.CharField(max_length=70, default='coding')
    thumbnail_des = models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('home')
        
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Group(models.Model):
    title = models.CharField(max_length=50)
    user = models.ManyToManyField(User,)
    description = models.TextField(max_length=200)    
    


    def __str__(self):
        return self.title 
        
class Category(models.Model):
    name = models.CharField(max_length=50)
    group = models.ManyToManyField(Group, related_name='categorys')
    def __str__(self):
        return self.name
    


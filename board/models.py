from typing import Callable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=250)
    classnmae=models.CharField(max_length=30,blank=True)
    civilid=models.BigIntegerField(blank=True)
    gender=models.CharField(max_length=20,blank=True)
    #created_at = models.DateField(auto_now=True)
    #updated_at = models.DateField(auto_now_add=True)   
    #schoolname=models.ForeignKey(school,related_name='school',on_delete=models.CASCADE,blank=)
    def __str__(self):
        return self.name


class absent(models.Model):
    #sessiontime=models.DateTimeField()
    #absentnmae=models.ForeignKey(Students,related_name='absentst',on_delete=CASCADE)
    absentname=models.CharField(max_length=50)
    #created_by=models.ForeignKey(User,name='absentst',on_delete=CASCADE)
    def __str__(self):
        return self.absentname
class absentstudent(models.Model):
    #sessiontime=models.DateTimeField()
    #absentnmae=models.ForeignKey(Students,related_name='absentst',on_delete=CASCADE)
    absentname=models.CharField(max_length=50)
    #created_by=models.ForeignKey(User,name='absentst',on_delete=CASCADE)
    def __str__(self):
        return self.absentname


    




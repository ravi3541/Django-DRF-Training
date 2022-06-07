from inspect import modulesbyfile
from django.db import models


# Course Model
class Course(models.Model):
    cname = models.CharField(max_length=20,unique=True)
    duration = models.IntegerField()
    pattern = models.IntegerField()
    desc  = models.CharField(max_length=200)

    def __str__(self):
        return self.cname


# Student Model
class Student(models.Model):
    sname = models.CharField(max_length=70)
    rollno = models.IntegerField(unique=True)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    mob = models.CharField(max_length=10,unique=True)
    course = models.OneToOneField(Course,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rollno) + self.sname
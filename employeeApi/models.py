from django.db import models

# Create your models here.

class Employee(models.Model):
    ename = models.CharField(max_length = 30, null= False)
    designation = models.CharField(max_length = 50, null=False)
    addr = models.TextField(max_length = 100,null= False)
    salary = models.IntegerField(null=False)

    def __str__(self):
        return self.ename

    

class Project(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    deadline = models.DateField()
    emp = models.ManyToManyField(Employee)

    def __str__(self):
        return self.title

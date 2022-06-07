from django.db import models

# Employee Model

class Employee(models.Model):
    ename = models.CharField(max_length = 30, null= False)
    designation = models.CharField(max_length = 50, null=False)
    addr = models.TextField(max_length = 100,null= False)
    salary = models.IntegerField(null=False)

    # function to return employee name 
    def __str__(self):
        return self.ename

    

# Project Model

class Project(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200)
    deadline = models.DateField()
    emp = models.ManyToManyField(Employee)

    # function to return Project Title
    def __str__(self):
        return self.title

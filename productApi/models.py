from django.db import models

# Product Model
class Product(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    brand =models.CharField(max_length=50)

    def __str__(self):
        return self.title



# Customer model
class Customer(models.Model):
    name = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    pin = models.CharField(max_length=6)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here. Representations of your DB schema - SQL tables
#python3 manage.py startapp listings created the listings folder which is considered an app

class Listing(models.Model): #This line creates the model, always will inherit from models.Model, below are the columns in the table which is the info you want stored (attributes)
    title = models.CharField(max_length=150) #CharField lets django know that its a string
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self): #To string method - specifically for django, will return the title of the model whenever its represented as a string
        return self.title
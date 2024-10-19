from django.contrib import admin
from .models import Listing

# Register your models here.
admin.site.register(Listing) #This line registers the model with the admin site so that it can be viewed and edited, good practice to do every time
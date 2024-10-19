from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm): #Create a form that inherits from ModelForm
    class Meta: #Meta class is used to configure the form, required when using ModelForm
        model = Listing #The model this form is associated with
        fields = ['title', 
                  'price', 
                  'num_bedrooms', 
                  'num_bathrooms', 
                  'square_footage', 
                  'address',
                  'image'
        ] #Fields to include in the form
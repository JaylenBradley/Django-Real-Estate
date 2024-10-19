from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm
# Create your views here. Logic to handle what happens when a user goes to a page on your site
#CRUD - create, retrieve, update, delete, list (actions you want to perform to the DB)

#Can either use function based views or class based views, function shows more information while class is more simplified as django handles it
def listing_list(request): #Create function - Convention to have the function name after the name of the model, request must always be passed
    listings = Listing.objects.all().order_by('price') #Query the DB to get all the listings, order by price
    context = {
        'listings': listings #Pass the listings to the template for rendering, key value pairs
    }
    return render(request, 'listings.html', context) #Render the request, the template, and the context. Render gets returned to the user as a response

def listing_retrieve(request, id): #Retrieve function - id gets passed from auto creation in migrations
    listing = Listing.objects.get(id=id) #Get specific listing, id(new val) = id(passed from function)
    context = {
        'listing': listing
    }
    return render(request, 'listing.html', context)

def listing_create(request):
    form = ListingForm() #Instantiates the form which calls it to create a new form, starts w empty form by default
    if request.method == 'POST': #If the form has been submitted
        form = ListingForm(request.POST, request.FILES) #Passes in the data and files from the form/post request
        if form.is_valid(): 
            form.save() #Save the new listing to the DB
            return redirect('/') #Redirect to the home/listings page after saving
    
    context = {
        "form" : form
    }
    return render(request, 'listing_create.html', context) #Render the form to the user, {'form': form} is another way to pass context without creating it separately

def listing_update(request, id):
    listing = Listing.objects.get(id=id)
    form = ListingForm(instance=listing) #Pass in the instance of the listing to the form
    if request.method == 'POST': 
        form = ListingForm(request.POST, files=request.FILES, instance=listing) #Submitting the form to this post request 
        if form.is_valid(): 
            form.save() 
            return redirect('/') 
    
    context = {
        "form" : form
    }
    return render(request, 'listing_update.html', context) 

def listing_delete(request, id):
    listing = Listing.objects.get(id=id)
    listing.delete()
    return redirect('/')
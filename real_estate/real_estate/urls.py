"""
URL configuration for real_estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from listings.views import (
    listing_list, 
    listing_retrieve, 
    listing_create, 
    listing_update,
    listing_delete
    ) #imports the view created

urlpatterns = [ #add paths here to link to different pages on your site
    path('admin/', admin.site.urls),
    path('', listing_list), #2nd argument is the name of the function your using for the path, empty path = homepage
    path('listings/<id>', listing_retrieve), #<id> is a variable that gets passed to the function, if name was diff would have to change in function
    path('listings/<id>/edit/', listing_update),  
    path('listings/<id>/delete/', listing_delete),  
    path('add-listing/', listing_create), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
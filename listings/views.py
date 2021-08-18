from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Listing


def index(request):
    # listings=Listing.objects.order_by('id')  # fetching all listing objects from database
    listings=Listing.objects.order_by('-list_date')  # fetching all listing objects from database

    paginator=Paginator(listings, 6)  # creating a paginator object
    page=request.GET.get('page')     # getting the desired page number from url
    paged_listings=paginator.get_page(page) #returns the desired page object
    context={'listings':paged_listings}
    return render(request, 'listings/listings.html',context)


def listing(request, listing_id):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')

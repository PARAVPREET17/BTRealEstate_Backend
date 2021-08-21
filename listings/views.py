from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from .choices import price_choices,state_choices,bedroom_choices

def index(request):
    # listings=Listing.objects.order_by('id')  # fetching all listing objects from database
    # fetching all listing objects from database
    listings = Listing.objects.order_by('-list_date')

    paginator = Paginator(listings, 3)  # creating a paginator object
    # getting the desired page number from url
    page = request.GET.get('page')
    # returns the desired page object
    paged_listings = paginator.get_page(page)
    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html',context)


def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)

    #City        
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city__iexact=city) #iexact :case-insensitive , exact:case-sensitive
    #State 
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state) 
    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(description__lte=bedrooms)        #lte=less than or equal to      
    #Price
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            queryset_list=queryset_list.filter(description__icontains=price)
    context={
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
        'listings':queryset_list,
        'values':request.GET
    }
    return render(request, 'listings/search.html',context)

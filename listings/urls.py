from django.urls import path

from . import views

urlpatterns =[ 
    path('',views.index,name='listings'),
    path('<int:listing_id>',views.listing,name='listing'),#To capture a value from the URL, use angle brackets.
    path('search',views.search,name='search'),
]
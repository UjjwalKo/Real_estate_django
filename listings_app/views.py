from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import Listing

# Create your views here.
def index(request):
    paginator = Paginator(Listing.objects.all(), 6)            # Paginator is used to display the data in the page
    page = request.GET.get('page')                             # Get the page number from the url
    paged_listings = paginator.get_page(page)                  # Get the data from the database according to the page number
    context = {
        'listings' : paged_listings                         # Fetch all the data from the database
    }
    return render(request, "listings_app/listings.html", context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing' : listing
    }
    return render(request, "listings_app/listing.html", context)
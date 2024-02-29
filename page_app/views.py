from django.shortcuts import render
from listings_app.models import Listing
from broker_app.models import Broker

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-post_date')[:3]
    context = {
        'listings': listings
    }
    return render(request, "page_app/index.html", context)

def about(request):
    brokers = Broker.objects.all()
    
    context = {
        'brokers': brokers
    }
    return render(request, "page_app/about.html", context)
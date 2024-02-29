from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdm(admin.ModelAdmin):                      # To make id, title, is_published and other visible in admin panel.
    list_display = ('id', 'title', 'broker', 'is_published', 'price')
    list_display_links = ('id', 'title')                               # title and id can acts as link for opening edit page.
    list_filter = ('broker',)                                          # filtering by the name of broker
    list_editable = ('is_published',)                                  # We can pubish and unpublish the list of property
    list_per_page = 25


admin.site.register(Listing, ListingAdm)
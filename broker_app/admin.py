from django.contrib import admin
from .models import Broker

# Register your models here.
class BrokerAdm(admin.ModelAdmin):                      # To make id, name, and email visible in admin panel.
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')                 # name and id can acts as link for opening edit page.
    list_per_page = 25

admin.site.register(Broker, BrokerAdm)

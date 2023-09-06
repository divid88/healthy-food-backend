from django.contrib import admin

from .models import CustomerAddress, FavoriteVendor


admin.site.register(CustomerAddress)

admin.site.register(FavoriteVendor)

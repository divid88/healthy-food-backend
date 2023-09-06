from django.contrib import admin

from .models import City, Vendor, VendorAddress, WorkTime

admin.site.register(City)

admin.site.register(VendorAddress)


class VendorAddressInline(admin.TabularInline):
    model = VendorAddress


class WorkTimeInline(admin.TabularInline):
    model = WorkTime


class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'id','city', 'is_active', 'modified')
    inlines = (VendorAddressInline, WorkTimeInline)


admin.site.register(Vendor, VendorAdmin)

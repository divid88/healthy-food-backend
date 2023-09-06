from django_filters.rest_framework import FilterSet

from .models import Vendor


class VendorFilter(FilterSet):
    class Meta:
        model = Vendor
        fields = {
            'name': ['contains'],
            'food_type__name': ['contains']
            }



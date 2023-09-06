from django.db.models.signals import post_save

from menus.models import MenuVendor
from .models import Vendor


def create_menu(sender, instance, created, **kwargs):
    if created:
        MenuVendor.objects.create(vendor=instance)


post_save.connect(create_menu, sender=Vendor)

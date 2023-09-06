from django.db import models
from accounts.models import CustomUser

from vendors.models import City, Vendor


class CustomerAddress(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    city = models.ForeignKey(City, on_delete=models.RESTRICT, related_name='customers')
    address = models.CharField(max_length=200)
    post_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.city.name} - {self.address}'


class FavoriteVendor(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='favorites')
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='favorites')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer.username}'

    @classmethod
    def toggle_vendor(cls, customer, vendor):
        existing = cls.objects.filter(customer=customer, vendor=vendor)
        if existing:
            existing.delete()
        else:
            cls.objects.create(customer=customer, vendor=vendor)














# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from .managers import CustomUserManager
#
#
# class CustomUserMobile(AbstractUser):
#     username = models.CharField(unique=True, max_length=255)
#     mobile_number = models.CharField(unique=True, max_length=10)
#
#     is_admin = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'username'
#
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.username
#
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_module_perms(self, app_label):
#         return True
#


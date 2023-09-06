from django.db import models

from vendors.models import Vendor


class MenuVendor(models.Model):
    vendor = models.OneToOneField(Vendor, on_delete=models.CASCADE, related_name='menu')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor.name


class FoodCategory(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='categories/images/', null=True, blank=True)
    logo = models.ImageField(upload_to='categories/logos/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FoodType(models.Model):
    name = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='food_type', null=True, blank=True)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='food_types', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    menu = models.ForeignKey(MenuVendor, on_delete=models.CASCADE, related_name='foods')
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    price = models.PositiveBigIntegerField()
    is_available = models.BooleanField(default=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='foods/images')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.menu.vendor.name} - {self.food_type.name} - {self.name} '

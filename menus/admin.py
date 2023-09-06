from django.contrib import admin

from .models import FoodType, Food, MenuVendor, FoodCategory


admin.site.register(Food)
admin.site.register(FoodCategory)
admin.site.register(FoodType)
admin.site.register(MenuVendor)

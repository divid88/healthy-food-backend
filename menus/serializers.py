from rest_framework import serializers

from .models import FoodType, Food, MenuVendor, FoodCategory


class FoodAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['id', 'name', 'vendor', 'category']


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['id', 'name']


class FoodCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategory
        fields = ['id', 'name', 'logo', 'image']


class FoodsSerializers(serializers.ModelSerializer):
    food_type = FoodTypeSerializer()
    category = serializers.SerializerMethodField()

    def get_category(self, obj):
        cat = obj.food_type.category
        return cat.id

    class Meta:
        model = Food
        fields = ['id', 'name', 'price', 'is_available', 'description', 'image', 'food_type', 'category']


class MenuVendorSerializer(serializers.ModelSerializer):
    foods = FoodsSerializers(many=True)

    class Meta:
        model = MenuVendor
        fields = ['id', 'foods']



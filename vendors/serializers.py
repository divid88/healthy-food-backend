import datetime
from rest_framework import serializers

from .models import City, Vendor, VendorAddress, WorkTime
from menus.serializers import FoodTypeSerializer, MenuVendorSerializer


class AvailableCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorAddress
        fields = ['address_line1']


class TimeVendorAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        excludes = ['created', 'modified']

    def create(self, validated_data):
        print(validated_data)
        vendor = Vendor.objects.get(pk=10)
        instance = WorkTime.objects.create(vendor=vendor, **validated_data)
        return instance


class ListVendorSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    addresses = AddressSerializer(many=True)
    open_times = serializers.SerializerMethodField(read_only=True)
    hour_opening = serializers.SerializerMethodField(read_only=True)
    menu = MenuVendorSerializer()

    def get_open_times(self, obj):
        day = datetime.datetime.now().weekday()
        try:
            result = obj.open_times.filter(day=day)[0].check_open()
        except:
            return None

    def get_hour_opening(self, obj):
        day = datetime.datetime.now().weekday()
        try:
            hour = obj.open_times.filter(day=day)[0].hour_opening()
            if hour:
                return hour + 'امروز'
            else:
                new_day = day + 1 if day < 6 else 0
                hour = obj.open_times.filter(day=new_day)[0].hour_opening()
                return str(hour) + 'فردا'
        except:
            return None

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'city', 'logo', 'delivery', 'menu', 'is_active', 'profile_image', 'addresses', 'open_times', 'hour_opening']


class VendorMenuSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    addresses = AddressSerializer(many=True)
    menu = serializers.SerializerMethodField(read_only=True)
    food_type = FoodTypeSerializer(many=True)
    open_times = serializers.SerializerMethodField(read_only=True)
    hour_opening = serializers.SerializerMethodField(read_only=True)

    def get_open_times(self, obj):
        day = datetime.datetime.now().weekday()
        return obj.open_times.filter(day=day)[0].check_open()

    def get_hour_opening(self, obj):
        day = datetime.datetime.now().weekday()
        hour = obj.open_times.filter(day=day)[0].hour_opening()
        if hour:
            print(hour)
            return hour + 'امروز'
        else:
            new_day = day + 1 if day < 6 else 0
            print(new_day)
            hour = obj.open_times.filter(day=new_day)[0].hour_opening()
            print("tomarow", hour)
            return str(hour) + 'فردا'

    def get_menu(self, obj):
        menu_vendor = obj.menu
        serializer = MenuVendorSerializer(menu_vendor)
        return serializer.data

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'city', 'logo', 'is_active', 'open_times', 'profile_image', 'addresses', 'hour_opening',
                  'menu', 'food_type']


class VendorFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name']


class RegisterVendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendor
        fields = ['id', 'name', 'logo', 'delivery', 'delivery', 'profile_image']


class VendorRetrieveSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)


    class Meta:
        model = Vendor
        fields = ['id', 'name', 'city', 'logo', 'profile_image', 'addresses']
from rest_framework import serializers

from .models import OrderItem, Order
from menus.serializers import FoodsSerializers

from customer.serializers import AddressSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    food = FoodsSerializers()

    class Meta:
        model = OrderItem
        fields = ['food', 'qty', 'price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    shipping_address = AddressSerializer()

    class Meta:
        model = Order
        fields = ['id', 'customer', 'is_paid', 'payment_method', 'items', 'shipping_address', 'total_price']


class ReportOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'is_paid', 'total_price', 'created']

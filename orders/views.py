from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from customer.models import CustomerAddress
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import OrderSerializer, ReportOrdersSerializer
from .models import Order, OrderItem
from menus.models import Food
from django.utils import timezone


class OrderCustomerAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        address = CustomerAddress.objects.get(pk=data['shipping_address'])
        order = Order.objects.create(customer=user, shipping_address=address)
        cart_items = data['cart_items']
        total_price = 0
        for item in cart_items:
            food = Food.objects.get(pk=item['id'])
            OrderItem.objects.create(order=order, food=food, qty=item['qty'], price=item['price'])
            total_price += item['price']
        order.total_price = total_price
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class OrderRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        order = Order.objects.get(pk=kwargs['pk'])
        cart_items = data

        total_price = order.total_price
        for item in cart_items:
            food = Food.objects.get(pk=item['id'])
            OrderItem.objects.create(order=order, food=food, qty=item['qty'], price=item['price'])
            total_price += item['price']
        order.total_price = total_price
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class ReportOrderAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReportOrdersSerializer

    def get_queryset(self):
        customer = self.request.user
        orders = Order.objects.filter(customer=customer)
        return orders

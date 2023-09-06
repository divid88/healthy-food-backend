from django.db import models
from accounts.models import CustomUser
from customer.models import CustomerAddress
from menus.models import Food


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    payment_method = models.CharField(max_length=30, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    total_price = models.PositiveBigIntegerField(null=True, blank=True)
    shipping_address = models.ForeignKey(CustomerAddress, on_delete=models.RESTRICT, related_name='order')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer.username}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="orders")
    qty = models.PositiveSmallIntegerField()
    price = models.PositiveBigIntegerField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.food} - {self.qty}'

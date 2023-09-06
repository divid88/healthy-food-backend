from django.db import models

from orders.models import Order


class Payments(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    author = models.CharField(max_length=200, null=True, blank=True)
    is_paid = models.BooleanField(default=False, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    modified = models.DateTimeField(auto_now=True, verbose_name="زمان آپدیت")
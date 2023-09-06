from django.db.models.signals import post_save

from payments.models import Payments
from orders.models import Order


def create_payment(sender, instance, created, **kwargs):
    if created:
        Payments.objects.create(order=instance, amount=0)
    Payments.objects.filter(order=instance).update(amount=instance.total_price)


post_save.connect(create_payment, sender=Order)

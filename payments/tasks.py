from celery import shared_task
from django.db.models import Sum

from django.utils import timezone
from .models import Payments


@shared_task()
def sample_task():
    pass


@shared_task(name='get_and_send_total_purchase')
def get_and_send_total_purchase():
    payment = Payments.objects.filter(is_paid=True).aggregate(total=Sum('amount'))

    print(f"Payment total : {payment.get('total', 0)}")

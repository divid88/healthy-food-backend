from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Payments
from orders.models import Order
from .serializers import PaymentSerializer
from .utiles import request_payment, verify_payment


class PaymentRequestAPIView(APIView):
    def post(self, request):
        data = request.data
        order_id = data['id']
        order = get_object_or_404(Order, id=order_id)
        payment_element = Payments.objects.get(order=order)
        if order.is_paid:
            raise Http404
        elif data['paid']:
            order.is_paid = True
            order.save()
        return Response({'id': payment_element.id, 'paid': order.is_paid}, status=status.HTTP_202_ACCEPTED)
    # def post(self, request):
    #     data = request.data
    #     order_id = data['id']
    #     order = get_object_or_404(Order, id=order_id)
    #     payment_element = Payments.objects.get(order=order)
    #     if order.is_paid:
    #         raise Http404
    #     res = request_payment(request, order.total_price, order.customer.username,
    #                           f"http://localhost:3000/payments/{payment_element.id}/")
    #     author = res[1]
    #     payment_element.author = author
    #     payment_element.save()
    #     return Response({'id': payment_element.id, 'red': res[0]}, status=status.HTTP_200_OK)


class PaymentVerifyAPIView(APIView):

    def get(self, request, *arg, **kwarg):
        payment = Payments.objects.get(pk=kwarg['pk'])
        author = payment.author
        response = verify_payment(request, author)

        if response.status_code == 200:
            payment.order.is_paid = True
            payment.is_paid = True
            payment.order.save()

        serializer = PaymentSerializer(payment)
        return Response(serializer.data)


class PaymentAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        order_id = data['id']
        order = Order.objects.get(pk=order_id)
        payment = Payments.objects.get(order=order)
        paid = data['paid']
        if paid:
            payment.is_paid = True
            order.is_paid = True
            payment.save()
            order.save()
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

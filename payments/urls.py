from django.urls import path

from . import views

urlpatterns = [
    path('payment_request/', views.PaymentRequestAPIView.as_view(), name='payment_request'),
    path('payment_varify/<int:pk>/', views.PaymentVerifyAPIView.as_view(), name='payment_verify'),
    path('payment/', views.PaymentAPIView.as_view(), name="payment")
]

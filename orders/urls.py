from django.urls import path


from . import views


urlpatterns = [
    path('create/', views.OrderCustomerAPIView.as_view(), name='create_order'),
    path('detail/<int:pk>/', views.OrderRetrieveAPIView.as_view(), name='detail_order'),
    path('report_order/', views.ReportOrderAPIView.as_view(), name="report_serializer")

]
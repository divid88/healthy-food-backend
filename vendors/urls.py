from django.urls import path

from . import views

urlpatterns = [
    path('cities/', views.ListAvailableCityAPIView.as_view(), name='cities'),
    path('register/', views.RegisterVendorAPIView.as_view(), name='register_vendor'),
    path('vendors/<int:pk>/', views.ListVendorCity.as_view(), name='city_vendors'),
    path('menu/<int:pk>/', views.VendorMenuAPIView.as_view(), name='vendor_menu'),
    path('time_add/', views.AddUpdateTimeVendor.as_view(), name='add_time'),
    path('admin-vendor/', views.AdminVendor.as_view(), name='admin-vendor'),
]

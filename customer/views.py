from rest_framework import status
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import CustomUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .models import CustomerAddress, FavoriteVendor
from .serializers import MyTokenObtainPairSerializer, AddressSerializer, FavoriteVendorSerializer
from vendors.models import City, Vendor


class LoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class AddAddressAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = AddressSerializer
    queryset = CustomerAddress.objects.all()

    def post(self, request, *args, **kwargs):
        print(request.data)
        customer = request.user
        data = request.data
        city = City.objects.get(pk=data['city'])
        address = CustomerAddress.objects.create(customer=customer, city=city, address=data['address'],
                                                 post_code=data['post_code'])
        serializer = AddressSerializer(address)
        return Response(serializer.data)


class ToggleFavorite(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = JWTAuthentication

    def post(self, request,):
        customer = request.user
        data = request.data
        vendor_id = data['vendor_id']
        vendor = Vendor.objects.get(pk=vendor_id)
        if vendor not in customer.favorites.all():
            favorite = FavoriteVendor.objects.create(customer=customer, vendor=vendor)
            serializer = FavoriteVendorSerializer(favorite)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail': 'An error has occurred'}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFavorite(DestroyAPIView):
    permission_classes = (IsAuthenticated, )

    def delete(self, request, *args, **kwargs):
        customer = request.user
        vendor_id = kwargs['vendor_id']
        vendor = Vendor.objects.get(pk=int(vendor_id))
        favorite = FavoriteVendor.objects.filter(customer=customer, vendor=vendor)
        if favorite:
            print("ok")
            print(favorite)
            favorite[0].delete()
            favorites = customer.favorites.all()
            print(favorites)
            serializer = FavoriteVendorSerializer(favorites, many=True)
            return Response(serializer.data, status=status.HTTP_207_MULTI_STATUS)
        else:
            return Response({'detail': 'An error has occurred'}, status=status.HTTP_400_BAD_REQUEST)

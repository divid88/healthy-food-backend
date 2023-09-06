from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.views.decorators.cache import cache_page

from .models import City, Vendor, WorkTime, VendorAddress
from .serializers import AvailableCitySerializer, ListVendorSerializer, VendorMenuSerializer, TimeVendorAddSerializer, \
    RegisterVendorSerializer, VendorRetrieveSerializer
from .filters import VendorFilter


@method_decorator(cache_page(60 * 10), name='get')
class ListAvailableCityAPIView(ListAPIView):
    queryset = City.objects.filter(is_active=True)
    serializer_class = AvailableCitySerializer


class ListVendorCity(ListAPIView):
    serializer_class = ListVendorSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = VendorFilter
    search_fields = ['name', 'food_type__name', 'food_type__items__name']

    def get_queryset(self, **kwargs):
        return Vendor.objects.filter(city_id=self.kwargs['pk'])


class VendorMenuAPIView(RetrieveAPIView):

    def get(self, request, **kwargs):
        vendor = Vendor.objects.get(pk=self.kwargs['pk'], is_active=True)
        ser = VendorMenuSerializer(vendor)
        return Response(ser.data, status=status.HTTP_200_OK)

    # def get_queryset(self):
    #     return Vendor.objects.get(pk=self.kwargs['pk'])


class RegisterVendorAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = RegisterVendorSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        city_pk = int(''.join(data.pop('city')))
        address_line1 = ''.join(data.pop('address_line1'))
        city = City.objects.get(pk=city_pk)
        vendor = Vendor.objects.create(user=request.user, city=city, name=data['name'],
                                       delivery=int(''.join(data.pop('delivery'))),
                                       profile_image=data['profile_image'],
                                       logo=data['logo'])
        address = VendorAddress.objects.create(vendor=vendor, address_line1=address_line1)
        return Response(status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        user = self.request.user
        user.is_vendor = True
        user.save()
        serializer.save(user=user)


class AddUpdateTimeVendor(CreateAPIView, RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = WorkTime.objects.all()
    serializer_class = TimeVendorAddSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        vendor = Vendor.objects.get(user=user)
        for day in data:
            WorkTime.objects.create(vendor=vendor, **day)
        return Response(status=status.HTTP_200_OK)


class AdminVendor(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        vendor = Vendor.objects.get(user=user)
        serializer = VendorMenuSerializer(vendor)
        return Response(serializer.data)


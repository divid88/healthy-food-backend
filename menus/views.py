from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import FoodCategory, FoodType, Food
from .serializers import FoodCategorySerializer, FoodAddSerializer, FoodTypeSerializer
from vendors.models import Vendor


class CategoryFoodAPIView(ListAPIView):
    queryset = FoodCategory.objects.all()[:10]
    serializer_class = FoodCategorySerializer


class AddTypeFoodAPIView(CreateAPIView, RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        vendor = Vendor.objects.get(user=user)
        category = FoodCategory.objects.get(pk=self.request.data['category'])
        instance = FoodType.objects.create(vendor=vendor, category=category, name=self.request.data['name'])
        serializer = FoodAddSerializer(instance)

        return Response(serializer.data)

    def get(self):
        vendor = Vendor.objects.get(pk=10)
        instance = vendor.food_type.all()
        serializer = FoodTypeSerializer(instance)
        return Response(serializer.data)


class AddFoodAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        user = request.user
        vendor = Vendor.objects.get(user=user)
        data = request.data
        print(data)
        food_type = int(''.join(data.pop('food_type')))
        food_type = FoodType.objects.get(pk=food_type)
        Food.objects.create(food_type=food_type, name=data['name'], description=data['description'],
                            price=int(''.join(data['price'])), image=data['image'], menu=vendor.menu)
        return Response(status=status.HTTP_201_CREATED)

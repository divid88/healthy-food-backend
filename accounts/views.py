from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.views import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import MyTokenObtainPairSerializer, RegisterUserSerializer
from .models import CustomUser


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterCustomUser(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data['email']
        data['first_name'] = email.split('@')[0]
        data['last_name'] = email.split('@')[0]
        data['username'] = email.split('@')[0]
        instance = CustomUser.objects.create_user(**data)
        instance.is_active = True
        instance.save()
        serializer = RegisterUserSerializer(instance)
        return Response(serializer.data)






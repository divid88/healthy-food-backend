from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views


urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('address/', views.AddAddressAPIView.as_view(), name='address'),
    path('toggle_favorite/', views.ToggleFavorite.as_view(), name='toggle_views'),
    path('delete_favorite/<str:vendor_id>/', views.RemoveFavorite.as_view(), name='delete_favorite'),
    # path('user/', views.UserAPIView.as_view(), name='user'),
]

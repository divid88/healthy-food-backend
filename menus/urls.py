from django.urls import path

from . import views

urlpatterns = [
    path('food_category/', views.CategoryFoodAPIView.as_view(), name='category_foods'),
    path('type_food/', views.AddTypeFoodAPIView.as_view(), name='add_type_food'),
    path('add_food/', views.AddFoodAPIView.as_view(), name='add_food'),
]

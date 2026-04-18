from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_list, name='shop_list'),
    path('create/', views.shop_create, name='shop_create'),
    path('<int:pk>/', views.shop_detail, name='shop_detail'),
    path('<int:pk>/update/', views.shop_update, name='shop_update'),
    path('<int:pk>/delete/', views.shop_delete, name='shop_delete'),
]

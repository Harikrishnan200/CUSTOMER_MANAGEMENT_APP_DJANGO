from django.urls import path
from . import views
urlpatterns = [
    
    path('products/', views.products,name='products'),
    path('', views.dashboard,name='dashboard'),
    path('customer/<pk>/', views.customer,name='customer'),
    
]
from django.urls import path
from . import views
urlpatterns = [
    
    path('products/', views.products,name='products'),
    path('', views.dashboard,name='dashboard'),
    path('customer/<pk>/', views.customer,name='customer'),
    path('update/<pk>/', views.update,name='update'),
    path('create/', views.create,name='create'),
    path('remove/<pk>/', views.remove,name='remove'),
    
]
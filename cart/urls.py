from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    # path('add_cart/', views.add_cart, name='add_cart'),  
    path('add_cart_ajax/', views.add_cart_ajax, name='add_cart_ajax'),  
] 

from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart_page', views.cart_page, name='cart_page'),
    path('cart/add_cart/<int:product_id>/<int:variant_id>/', views.add_cart, name='add_cart'),

 
] 

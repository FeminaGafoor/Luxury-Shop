from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('cart/',views.cart,name='cart'),
    path('add_cart/',views.add_cart,name='add_cart'),
]
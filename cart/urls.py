from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart_page', views.cart_page, name='cart_page'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    # path('update_cart/', views.update_cart, name='update_cart'),   
    path('delete_cart_product/<int:product_id>/<int:variant_id>/', views.delete_cart_product, name='delete_cart_product'),

 
] 

from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart_page', views.cart_page, name='cart_page'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    # path('update_quantity/<int:product_id>/<int:new_quantity>/', views.update_quantity, name='update_quantity'),    # path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('delete_cart_product/<int:product_id>/<int:variant_id>/', views.delete_cart_product, name='delete_cart_product'),

 
] 

from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('shop/',views.shop,name='shop'),
    path('product/<int:id>/', views.product, name='product'),
    path('category/',views.category,name='category'),
    path('womens/',views.womens,name='womens'),
    path('mens/',views.mens,name='mens'),
    path('kids/',views.kids,name='kids'),
    path('search/',views.search,name='search'),
   


    
    
]
    
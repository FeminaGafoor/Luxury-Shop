from django.urls import path
from . import views

app_name='orders'


urlpatterns = [
    path('place_order',views.PlaceOrderView.as_view(),name='place_order'),
   
]
    
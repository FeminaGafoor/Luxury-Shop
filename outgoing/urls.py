from django.urls import path
from . import views

app_name='outgoing'


urlpatterns = [
     path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),

    path('payments',views.payments,name='payments'),
    path('summary',views.summary,name='summary'),
    path('finish',views.finish,name='finish'),
]
    
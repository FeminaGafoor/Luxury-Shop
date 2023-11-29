from django.urls import path
from . import views

app_name='outgoing'


urlpatterns = [
    
    path('checkout/',views.checkout,name='checkout'),


    path('summary',views.summary,name='summary'),
    path('finish',views.finish,name='finish'),
]
    
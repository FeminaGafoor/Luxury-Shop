"""
URL configuration for newpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from cart import views as cartviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('items/',include('items.urls')),
    path('blog/',include('blog.urls')),
    path('aboutus/',include('aboutus.urls')),
    path('contact/',include('contact.urls')),    
    path('shop/',include('shop.urls')),
    path('account/',include('account.urls')),
    path('cart/',include('cart.urls')),
    path('outgoing/',include('outgoing.urls')),
    path('for_admin/',include('for_admin.urls')),
    path('update_cart/', cartviews.update_cart, name='update_cart'),   
    # ORDERS
    
    path('orders/',include('orders.urls')),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render

from items.models import Brand, MutipleImage, Product_variant, Products

# Create your views here.


def checkout(request):
    return render(request,'user/checkout.html')



def payments(request):
    return render(request,'user/payments.html')


def summary(request):
    return render(request,'user/summary.html')


def finish(request):
    return render(request,'user/finish.html')
from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request,'user/cart.html')

def checkout(request):
    return render(request,'user/checkout.html')



def payments(request):
    return render(request,'user/payments.html')


def summary(request):
    return render(request,'user/summary.html')


def finish(request):
    return render(request,'user/finish.html')
from django.shortcuts import render

from items.models import Brand, MutipleImage, Product_variant, Products

# Create your views here.

def cart(request):
    brand = Brand.objects.all()
    product = Products.objects.all()
    images = MutipleImage.objects.filter()
    product_variant = Product_variant.objects.all()
    print(brand,"++++++++++++++++++++++++++++++")
    print(product,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    product_display = Product_variant.objects.all()
    context = {
        'product' : product,
        'brand' : brand,
        'iamges' : images,
        'product_display' : product_display,
        'product_variant' : product_variant,
         
     }
    
    
    return render(request,'user/cart.html',context)

def add_cart(request):
    
    
    return render(request,'user/cart.html')
    
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from items.models import Category, Products,ProductImage


# Create your views here.


def shop(request):
    product = Products.objects.all()
    image = ProductImage.objects.all()
    context = {
        'product': product,
        'image': image,
    }
    return render(request, 'user/shop.html', context)



def product(request, product_id):
    print(f"Product view called with product_id={product_id}")
    
    image = ProductImage.objects.all()
    # Add any additional context you want to pass to the product.html template
    context = {
        'product': product,
        'image': image,
    }
  
    return render(request, 'user/product.html', context)


def category(request):
    category = Category.objects.all()
 
    context = {
        'category':category
    }
    return render(request,'user/categories.html',context)


def womens(request):
    women_products = Products.objects.filter(category__name='Women')

    context = {
        'women_products': women_products
    }

    return render(request,'user/womens.html',context)



def mens(request):
    men_products = Products.objects.filter(category__name='Men')
    
    context = {
        'men_products' : men_products
    }
    return render(request,'user/mens.html',context)


def kids(request):
    kid_products = Products.objects.filter(category__name='Kids')
    
    context = {
        'kid_products' : kid_products
    }
    return render(request,'user/kids.html',context)
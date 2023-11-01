from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from items.models import Brand, Category, Color, MutipleImage, Product_variant, Products,ProductImage, Size


# Create your views here.


def shop(request):
    product = Products.objects.all()
    # image = ProductImage.objects.all()
    context = {
        'product': product,
        # 'image': image,
    }
    return render(request, 'user/shop.html', context)



def product(request, product_id):
    context = {}
    
    product = Products.objects.get(id=product_id)
    image = MutipleImage.objects.filter(product=product_id)[0:3]
  
    product_variants = Product_variant.objects.filter(product=product_id)
    products = Products.objects.filter()
    colors = [variant.colors for variant in product_variants]
    sizes = [variant.size for variant in product_variants]
    
  
    print(f"Product Variants for Product ID {product_id}:")
    for variant in product_variants:
        print(f"Variant: {variant}, Color: {variant.colors}")


  
  
  
  
    print(product_variants)
    print(colors)
    print(sizes)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    context = {
        'product': product,
        'image': image,
        'product_variants' :product_variants,
        'colors' : colors,
        'size' : sizes,
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
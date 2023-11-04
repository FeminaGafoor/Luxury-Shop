from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from items.models import Brand, Category, Color, MutipleImage, Product_variant, Products, Size


# Create your views here.


def shop(request):
    product = Products.objects.all()
    # image = ProductImage.objects.all()
    context = {
        'product': product,
        # 'image': image,
    }
    return render(request, 'user/shop.html', context)



def product(request, id):
    query = request.GET.get('q')
    category = Category.objects.all()
    product = get_object_or_404(Products, id=id)

  
    images = MutipleImage.objects.filter(product=id)
    brand = Brand.objects.all()

    print("no variant")
    variants = Product_variant.objects.filter(product_id=id)
                
    product_colors = Product_variant.objects.filter(product_id=id)
    colors = set()
    # for i in product_colors:
    #     print(i.colors.name)
    #     colors.add(i.colors.code)
    for product_variant in product_colors:
        colors.add(product_variant.colors.code)
        print(product_variant.colors.name)

    print(colors)
                
    sizes = Product_variant.objects.filter(product_id=id, colors=product_colors[0].colors)
    print("calling")
    variant =Product_variant.objects.get(id=variants[0].id)

    print(images)
    for i in images:
        print(i.images)
        
        
    context={
        'category':category,
        'product':product,
       
        'images':images,
        'sizes': sizes, 
        'colors': colors,
        'variant': variant,
        'brand' : brand,
        'query': query,
    
    }
    
    return render(request, 'user/product.html',context)    


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

from django.core import serializers
import json
def ajaxcolor(request):
    data = {}
    if request.method == 'POST':
        size_id = request.POST.get('size')
        productid = request.POST.get('productid')
        s = Color.objects.get(code=size_id)
        print(s, 'size')
        colors = Product_variant.objects.filter(product_id=productid, colors=s)
        print(colors,   "color")
        # Serialize the QuerySet to JSON
        colors_json = serializers.serialize('json', colors)
        print(colors, 'colors')
        size = [item.size.name for item in colors]
        size_json = json.dumps(size)
        
        return HttpResponse(size_json, content_type='application/json')
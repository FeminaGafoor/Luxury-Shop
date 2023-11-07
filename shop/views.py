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
   
    for product_variant in product_colors:
        colors.add(product_variant.colors.code)
                
    colors= list(colors)
    sizes_ids = Product_variant.objects.filter(product_id=id, colors=product_colors[0].colors).values_list('size', flat=True)
    sizes = Size.objects.filter(id__in=sizes_ids)
    variant =Product_variant.objects.get(id=variants[0].id)
    product_variant=Product_variant.objects.all()
    print('Product Id ---->',id)
    print('Color    ---->',colors[0])
    initial_size = Product_variant.objects.filter(product_id=id, colors__code=colors[0]).first().size.name
    context={
        'category':category,
        'product':product,
        'product_variant':product_variant,
        'images':images,
        'sizes': sizes, 
        'colors': colors,
        'initial_color':colors[0] ,
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
        productid = request.POST.get('productid')
        colorid = request.POST.get('color')
        product_colors = Product_variant.objects.filter(product_id=productid,colors__code=colorid)
        size_ids = Product_variant.objects.filter(product_id=productid, colors=product_colors[0].colors).values_list('size', flat=True)
        sizes = Size.objects.filter(id__in=size_ids)
        sizes_serializer = []
        for size in sizes:
            sizes_serializer.append({'name':size.name,'id':size.id})
        sizes_json = json.dumps(sizes_serializer)
        return HttpResponse( sizes_json,content_type='application/json')
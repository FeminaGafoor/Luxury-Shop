from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from items.models import Banner, Brand, Category, Color, MultipleImage, Product_variant, Products, Size


# Create your views here.


def shop(request):
    product = Products.objects.all()
    image = MultipleImage.objects.all()
    # banner_images = Banner.objects.all()
    context = {
        'product': product,
        'image': image,
        # 'banner_images' : banner_images,
    }
    return render(request, 'user/shop.html', context)



def product(request, id):
    query = request.GET.get('q')
    category = Category.objects.all()
    product = Products.objects.get(id=id)
    brand = Brand.objects.all()

    variants = Product_variant.objects.filter(product_id=id)
    product_variant = variants.first()  # Select the first variant for simplicity

    product_colors = Product_variant.objects.filter(product_id=id)
    colors = set()
    colors_var_id = set()

    for product_variant in product_colors:
        color = product_variant.colors.first()
        if color:
            colors.add(color.code)
            colors_var_id.add(product_variant.id)

    colors = list(colors)

    data = zip(colors, list(colors_var_id))

    context = {
        'category': category,
        'product': product,
        'product_variant': product_variant,
        'colors': colors,
        'brand': brand,
        'query': query,
        'data': data,
    }

    return render(request, 'user/product.html', context)

  


def category(request):
    category = Category.objects.all()
    # banner_images = Banner.objects.all()
 
    context = {
        'category':category,
        # 'banner_images' : banner_images,
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

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def get_image_url(request, variant_id, color):
    image = get_object_or_404(MultipleImage, product_variant__id=variant_id, color__code=color)
    
    if image:
        image_url = image.images.url  # Assuming 'images' is the field holding the image URL
        return JsonResponse({'image_url': image_url})
    else:
        return JsonResponse({'error': 'Image not found'}, status=404)


























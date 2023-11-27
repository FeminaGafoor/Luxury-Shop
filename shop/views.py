from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from items.models import Banner, Brand, Category, Color, MultipleImage, Product_variant, Products, Size
from cart.models import Cart_Product
from cart.views import _cart_id
from django.db.models import Q


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
    product_variants = Product_variant.objects.filter(product_id=id)
    product_variant = product_variants.first()

    # Ensure you have a valid product_variant before proceeding
    if product_variant:
        in_cart = Cart_Product.objects.filter(cart__cart_id=_cart_id(request), product_variant=product_variant).exists()
        print(in_cart, "in_cart+++++++++++++++++++++++++++++++++++++")
    ajax_color = request.GET.get('color')
    
    print(ajax_color, "ajax color")

    product_variants = Product_variant.objects.filter(product_id=id)
    product_variant = product_variants.first()  # Select the first variant for simplicity
    
    product_colors = Product_variant.objects.filter(product_id=id)
    colors = set()
    sizes = set()
    colors_var_id = set()
    sizes_var_id = set()

    for product_variant in product_variants:
        color = product_variant.colors
        size = product_variant.size  # Access the color directly
        if color:
            colors.add(color.code)
            colors_var_id.add(product_variant.id)
            
        if size:
            sizes.add(size.name)
            sizes_var_id.add(product_variant.id)

    colors = list(colors)
    
    sizes = list(sizes)
    
    selected_color = Color.objects.get(code=colors[0])
    size = Product_variant.objects.get(product_id=id, colors=selected_color)
    
    if ajax_color:
        selected_color = Color.objects.get(code=ajax_color)
        filtered_data = Product_variant.objects.get(product_id=id, colors=selected_color)
        filtered_image = MultipleImage.objects.get(product_variant=filtered_data)

        print(filtered_image, 'new size')
        print(product_variant.price,"product_variant.price")
      
        
        return JsonResponse({ "size": filtered_data.size.name, "image": filtered_image.images.url, "variant_id": filtered_data.id})
    print(product_variants[0].id, "product variant id")
    context = {
        'variant_id': product_variants[0].id,
        'category': category,
        'product': product,
        'product_variant': product_variant,
        'colors': colors,
        'sizes': size.size.name,
        'brand': brand,
        'in_cart': in_cart,
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


def search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            products=Products.objects.order_by('create').filter(name__icontains=query)
            print(products,"products+++++++++++++++++++++++++++++")
            products_count = products.count()
            print(products_count,"products_count+++++++++++++++++++++++++++++")
    context = {
        'products' : products,
        'products_count' : products_count
    }        
  
    return render(request,'user/search.html',context)
























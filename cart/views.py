from audioop import reverse
import colorsys
import decimal
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from items.models import Brand, Color, Product_variant, Products
from account.models import User_Profile
from django.contrib.auth import get_user_model
from cart.models import Cart, Cart_Product



def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
              

def add_cart(request, product_id):
     
    product = Products.objects.get(id = product_id)
    variant_id = request.POST.get('variant_id')
    print("produc:",product)
    print("variant_id",variant_id)
    try :
        cart = Cart.objects.get(cart_id=_cart_id(request))
        
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        
        cart.save()
        
    if product.variant:
        
        variant_id = request.POST.get('variant_id')
        print(variant_id,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        check_variant = Cart_Product.objects.filter(product_variant = variant_id ,cart = cart)
        print("check_variant:",check_variant)
        if check_variant:
            control = 1
        else:
            control = 0
            
        if control == 1:  
            print('start')       
            cart_pro = Cart_Product.objects.get(product=product,cart=cart,product_variant=variant_id)
            
            cart_pro.quantity += 1
            print("cart_pro.quantity:",cart_pro.quantity)
            cart_pro.save()
        else:  
            print('end')   
            product = get_object_or_404(Products,id=product_id)
            print(product,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            variant = get_object_or_404(Product_variant,id=variant_id)
            print(variant,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            data = Cart_Product()
            data.quantity+=1
            data.product = product
            data.product_variant = variant
            print("data.product_variant :",data.product_variant )
            data.cart=cart
            data.save()
        

    # return HttpResponse(cart_pro.product.price)
    # exit()
    return redirect('cart:cart_page')
    
    
def cart_page(request, total=0, quantity=0, cart_pro=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_products = Cart_Product.objects.filter(cart=cart, is_active=True)
        print("cart_products:",cart_products)
        # Initialize cart_products before the loop
        for cart_pro in cart_products:
            # Assuming cart_pro.product_variant is a Product_variant object
            if cart_pro.product_variant:
                quantity += cart_pro.quantity
                total += cart_pro.sub_total
                print(cart_pro.product_variant,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                
                print(f"Product: {cart_pro.product.name}")
                print(f"Price: {cart_pro.product_variant.price}")
                print(f"Quantity: {cart_pro.quantity}")
                print(f"Subtotal: {cart_pro.sub_total}")
                
            tax = (2 * total)/100
            grand_total = total + tax
        context = {
            'total': total,
            'quantity': quantity,
            'cart_products': cart_products,
            'tax' : tax,
            'grand_total' : grand_total,
        }

    except ObjectDoesNotExist:
        # Initialize context if the cart doesn't exist
        context = {
            'total': total,
            'quantity': quantity,
            'cart_products': [],
            'tax': 0,
            
        }

    # Add brand_image information to each cart_pro in context
    for cart_pro in context['cart_products']:
        # Assuming cart_pro.product.brand is a Brand object
        cart_pro.brand_image = cart_pro.product.brand.brand_image.url if cart_pro.product.brand else None

    return render(request, 'user/cart.html', context)






def delete_cart_product(request, product_id, variant_id):
    if variant_id:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Products, id=product_id)
        variant = get_object_or_404(Product_variant, id=variant_id)
        
        cart_pro = Cart_Product.objects.get(product=product, cart=cart, product_variant=variant)
        
        cart_pro.delete()

    return HttpResponseRedirect(reverse('cart_page'))




# def orderproduct(request):
#         return render(request,'order_form.html')
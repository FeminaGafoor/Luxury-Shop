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
   
   
    

    try :
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
           
        )
        
        cart.save()
        
    if product.variant != 'None':
       
        variant_id = request.POST.get('variant_id')
        check_variant = Cart_Product.objects.filter(product_variant = variant_id ,cart = cart)
        if check_variant:
            control = 1
        else:
            control = 0
            
        if control == 1:  
            print('start')       
            cart_pro = Cart_Product.objects.get(product=product,cart=cart,product_variant=variant_id)
             
            cart_pro.quantity += 1
            cart_pro.save()
        else:  
            print('end')   
            product = get_object_or_404(Products,id=product_id)
            variant = get_object_or_404(Product_variant,id=variant_id)
            data = Cart_Product()
            data.product = product
            data.product_variant = variant
            data.cart=cart
            data.save()
        

    # return HttpResponse(cart_pro.product.price)
    # exit()
    return redirect('cart:cart_page')
    
    
def cart_page(request, total=0, quantity=0, cart_pro=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_products = Cart_Product.objects.filter(cart=cart, is_active=True)
        

        # Initialize cart_products before the loop
        for cart_pro in cart_products:
            # Assuming cart_pro.product_variant is a Product_variant object
            if cart_pro.product_variant:
                total += (cart_pro.product_variant.price * cart_pro.quantity)
                quantity += cart_pro.quantity

    except ObjectDoesNotExist:
        # Initialize cart_products if the cart doesn't exist
        cart_products = []

    context = {
        'total': total,
        'quantity': quantity,
        'cart_products': cart_products,
    }
    
    return render(request, 'user/cart.html', context)































# def remove_cart(request, id):
#     cart = Cart.objects.get(cart_id=cart_id(request))
#     variant = get_object_or_404(Product_variant, id=id)
#     cart_item = CartItem.objects.get(variant=variant, cart_item=cart)

#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         print(cart_item.quantity)
#         cart_item.save()
#     else:
#         cart_item.delete()
    
#     return redirect('cart:cart_page')




# def delete_cart_item(request,id):
#     cart=CartView.objects.get(cart_id=cart_id(request))
#     variant=get_object_or_404(Variants,id=id)
#     cart_item= ShopCart.objects.get(variant=variant,cart_item=cart)
#     cart_item.delete()
    
#     return HttpResponseRedirect('/cart_page')





# def orderproduct(request):
#         return render(request,'order_form.html')
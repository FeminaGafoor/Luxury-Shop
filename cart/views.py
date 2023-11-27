from audioop import reverse
import colorsys
import decimal
from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist
from items.models import Brand, Color, Product_variant, Products, MultipleImage
from account.models import User_Profile
from django.contrib.auth import get_user

from cart.models import Cart, Cart_Product




def _cart_id(request):
    cart = request.session.session_key

    if not cart:
        cart = request.session.create()
    return cart
              


def add_cart(request, product_id):
    current_user = request.user

    control = 0  # Initialize control variable
    variant_id = request.POST.get('variant_id')
    product = get_object_or_404(Products, pk=product_id)

    if current_user.is_authenticated:
       

    
            if product.variant != "None":
                variant_id = request.POST.get("variant_id")
                check_invariant = Cart_Product.objects.filter(
                    product_variant=variant_id, user=current_user
                )
                if check_invariant:
                    control = 1
                else:
                    control = 0    
            else:
                checkinproduct = Cart_Product.objects.filter(product=id, user=current_user)
                if checkinproduct:
                    control = 1
                else:
                    control = 0

            if control == 1:
                if product.variant == "None":
                    data = Cart_Product.objects.get(product=id, user=current_user)
                else:
                    data = Cart_Product.objects.get(
                         user=current_user, product_variant=variant_id
                    )
                data.quantity += 1  # Increment the quantity if the item already exists
                data.save()
            else:
                variant = get_object_or_404(Product_variant, id=variant_id)
                data = Cart_Product()
                data.product_variant = variant
                data.product = product
                data.user = current_user
                data.quantity = 1
                data.save()

            return redirect("cart:cart_page")
    else:
        try:
            cart = Cart.objects.get(
                cart_id=_cart_id(request),
            )

        except Cart.DoesNotExist:
            cart = Cart.objects.create(cart_id=_cart_id(request))

        cart.save()

        if product.variant != "None":
            variant_id = request.POST.get("variant_id")
            check_invariant = Cart_Product.objects.filter(product=product,
                product_variant=variant_id, cart=cart
            )
            if check_invariant:
                control = 1
            else:
                control = 0
        else:
            checkinproduct = Cart_Product.objects.filter(product=id, cart=cart)
            if checkinproduct:
                control = 1
            else:
                control = 0

        if control == 1:
            if product.variant == "None":
                data = Cart_Product.objects.get(product=product, cart=cart)
            else:
                data = Cart_Product.objects.get(
                     cart=cart, product_variant=variant_id
                )
            data.quantity += 1 
            data.save()
        else:
            variant = get_object_or_404(Product_variant, id=variant_id)
            data = Cart_Product()
            data.product = product
            data.product_variant = variant
            data.cart = cart  # No authenticated user in this case
            data.quantity = 1
            data.save()

    return redirect("cart:cart_page")
    
    
    
def cart_page(request, total=0, quantity=0, cart_pro=None):
    tax=0
    grand_total=0
    try:
        
        if request.user.is_authenticated:
            cart_products = Cart_Product.objects.filter(user=request.user)

        else:    
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_products = Cart_Product.objects.filter(cart=cart)

        cart_data = []
        for cart_product in cart_products:
            image = MultipleImage.objects.get(product_variant=cart_product.product_variant)
            cart_data.append((cart_product, image))
            if cart_product.product_variant:
                total +=(cart_product.product_variant.price * cart_product.quantity)
                quantity=cart_product.quantity
                

        # Now cart_data contains tuples where each tuple has a Cart_Product and its associated image
        # for cart_product, image in cart_data:
        #     # print("Cart Product:", cart_product.product_variant.product.name)
        #     print("Image:", image.images.url)
        # # Initialize cart_products before the loop
        # for cart_pro in cart_products:
        #     # Assuming cart_pro.product_variant is a Product_variant object
        #     if cart_pro.product_variant:
        #         quantity += cart_pro.quantity
        #         total += cart_pro.sub_total
        #         print(cart_pro.product_variant,"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                
        #         print(f"Product: {cart_pro.product.name}")
        #         print(f"Price: {cart_pro.product_variant.price}")
        #         print(f"Quantity: {cart_pro.quantity}")
        #         print(f"Subtotal: {cart_pro.sub_total}")
                
        tax = (2 * total)/100
        grand_total = total + tax
        context = {
            'total': total,
            'quantity': quantity,
            'cart_products': cart_products,
            'tax' : tax,
            'grand_total' : grand_total,
            'cart_data': cart_data,
        }

    except ObjectDoesNotExist:
        # Initialize context if the cart doesn't exist
        context = {
            'total': total,
            'quantity': quantity,
            'cart_products': [],
            'tax': 0,
            
        }

    return render(request, 'user/cart.html', context)


def update_cart(request,action,product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        if request.user.is_authenticated:
            print("hloo", product_id)
            product_v = Product_variant.objects.get(id=product_id)
            print(product_v, "product_v")
            cart_items = Cart_Product.objects.get(user=request.user, product_variant=product_v)
            print(cart_items, "cart")
        else:              
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items =Cart_Product.objects.filter(cart=cart)
   
        try:
            print(cart_items, "cart_item")
            cart_item = None
            if cart_items:
                print('if')
                #for cart_item in cart_items:  # Iterate over cart_items
        
                if action == "increase":
                        print('inc', int(cart_items.product_variant.stock), cart_items.quantity)
                        if int(cart_items.product_variant.stock) == cart_items.quantity:
                            print("if inc")
                            messages.error(request,'item empty')
                            return HttpResponseRedirect(url)
                            
                            # print(cart_item.variant.quantity)
                            # response_data={
                            #     'status':True,
                            #     'full':cart_item.variant.quantity,
                            # }
                            # return JsonResponse(response_data);
                            
                        else:
                            print("increa + ")
                            cart_items.quantity += 1

                        
                elif action == "decrease":
                        if cart_items.quantity > 1:
                            cart_items.quantity -= 1
                            
                        else:
                            messages.error(request, 'You can\'t order the product below 1')
                            # If cart_item.quantity <= 0:
                            # Remove the item from the cart if the quantity becomes zero or less
                            # cart_item.delete()
                else:
                        return HttpResponseBadRequest("Invalid action")

                cart_items.price = cart_items.product_variant.price * cart_items.quantity
                print(cart_items.price, cart_items.quantity)
                cart_items.save()

            # cart_items = Cart_Product.objects.filter(user=request.user)
            # cartQnty = sum(item.quantity for item in cart_items)
            # total = sum(item.variant.price for item in cart_items)
            # updated_price = cart_items.product_variant.price

      

            response_data = {
                'success': True,
                # 'qnty': cartQnty,
                'full': cart_items.quantity,  
                'price':cart_items.price,
                
              }
            return JsonResponse(response_data, status=200)
        except Exception as e:
            # Log the exception for debugging

            return JsonResponse({'error': 'Internal Server Error'}, status=500)
    else:
        return HttpResponseBadRequest("Cart item not found")
    
   


def delete_cart_product(request, product_id, variant_id):
    url = request.META.get('HTTP_REFERER')
    if variant_id:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Products, id=product_id)
        variant = get_object_or_404(Product_variant, id=variant_id)
        
        cart_pro = Cart_Product.objects.get(product=product, cart=cart, product_variant=variant)
        
        cart_pro.delete()

    return HttpResponseRedirect(url)




# def orderproduct(request):
#         return render(request,'order_form.html')
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from items.models import Brand, MultipleImage, Product_variant, Products
from cart.models import Cart, Cart_Product
from cart.views import _cart_id
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='account:user_login')
def checkout(request):
    total=0
    quantity=0
    tax=0
    grand_total=0
    try:
        if request.user.is_authenticated:
            cart_products = Cart_Product.objects.filter(user=request.user)
        else:    
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_products = Cart_Product.objects.filter(cart=cart, is_active=True)
        cart_data = []

        for cart_product in cart_products:
            image = MultipleImage.objects.get(product_variant=cart_product.product_variant)
            cart_data.append((cart_product, image))

        # Now cart_data contains tuples where each tuple has a Cart_Product and its associated image
        for cart_product, image in cart_data:
            print("Cart Product:", cart_product.product_variant.product.name)
            print("Image:", image.images.url)
        # Initialize cart_products before the loop
        for cart_pro in cart_products:
            # Assuming cart_pro.product_variant is a Product_variant object
            if cart_pro.product_variant:
                quantity += cart_pro.quantity
                # total += cart_pro.product_variant.price
                sub_total = sum(cart_pro.product_variant.price * cart_pro.quantity for cart_pro in cart_products)
                shipping=40
                print(f"Product: {cart_pro.product.name}")
                print(f"Price: {cart_pro.product_variant.price}")
                print(f"Quantity: {cart_pro.quantity}")
                print(f"Subtotal: {sub_total}")
                
            tax = (2 * sub_total)/100
            grand_total = sub_total + shipping + tax
            print(f"Grandtotal: {grand_total }")
                
            
        context = {
            'total': total,
            'quantity': quantity,
            'cart_products': cart_data,
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

    return render(request,'user/checkout.html',context)



def summary(request):
    return render(request,'user/summary.html')


def finish(request):
    return render(request,'user/finish.html')
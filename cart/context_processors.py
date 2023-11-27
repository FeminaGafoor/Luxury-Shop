from cart.views import _cart_id
from . models import Cart ,Cart_Product


def counter(request):
    cart_count = 0
    try:
        if request.user.is_authenticated:
            cart_pro = Cart_Product.objects.filter(user=request.user)
        else:    
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_pro = Cart_Product.objects.filter(cart=cart)
        for items in cart_pro:
            cart_count += items.quantity
            print(cart_count,"cart_count++++++++++++++++++++++++++++++++")
    except Cart.DoesNotExist:
        cart_count = 0
    return {"cart_count":cart_count}
        
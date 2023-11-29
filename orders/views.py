import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from cart.models import Cart_Product
from orders.models import Order
from orders.forms import Orderform

# Create your views here.


class PlaceOrderView(View):
    template_name = 'user/checkout.html'  # Update with your actual template name

    def get(self, request):
        current_user = request.user

        # if cart count is less than or equal to 0, then redirect back to shop
        cart_items = Cart_Product.objects.filter(user=current_user)
        cart_count = cart_items.count()
        if cart_count <= 0:
            return redirect('shop:shop')

        sub_total, quantity = self.calculate_totals(cart_items)

        context = {
            'sub_total': sub_total,
            'quantity': quantity,
            # Add any other context variables you need
        }

        return render(request, self.template_name, context)

    def post(self, request):
        current_user = request.user
        cart_items = Cart_Product.objects.filter(user=current_user)
        sub_total, quantity = self.calculate_totals(cart_items)

        tax = (2 * sub_total) / 100
        shipping = 40
        grand_total = sub_total + shipping + tax

        form = Orderform(request.POST)
         
        if form.is_valid():
            print("|||||||||||||||||") 
            data = Order()
            # ... (rest of your existing code for saving order data)

            return redirect('outgoing:checkout')
        else:
            # Handle form validation errors
            context = {
                'sub_total': sub_total,
                'quantity': quantity,
                'form': form,
                # Add any other context variables you need
            }
            return render(request, self.template_name, context)

    def calculate_totals(self, cart_items):
        sub_total = 0
        quantity = 0
        for cart_item in cart_items:
            sub_total += cart_item.product_variant.price * cart_item.quantity
            quantity += cart_item.quantity

        return sub_total, quantity
   
    # return render(request,'user/place_order.html')
    
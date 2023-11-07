import colorsys
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from items.models import Brand, Color, MutipleImage, Product_variant, Products
from cart.models import CartItem
from account.models import User_Profile
from django.contrib.auth import get_user_model


def cart(request):
    UserModel = get_user_model()
    user_instance = UserModel.objects.get(id=request.user.id)
    user_profile_instance = User_Profile.objects.get(user=user_instance)
    brand = Brand.objects.all()
    product = CartItem.objects.filter(customer=user_profile_instance)
    product_display = Product_variant.objects.all()
    print(product)
    context = {
        'cart' : product,
        'brand' : brand,
        'product_display' : product_display,
     }
    
    return render(request,'user/cart.html',context)




# def add_cart(request):
#     if request.method == "POST":
#         cart = []
#         id = request.POST['size_option']
#         print(id,"+++++++++++++++++++++++++++++++++++++++")
#         product_quantity = 1
#         product_variant = Product_variant.objects.get(id=id)
#         product_image = product_variant.product.image
#         product_description = product_variant.product.description
#         product_brand_image = product_variant.product.brand.brand_image
#         product_color = product_variant.colors.name
#         product_size = product_variant.size.name
#         product_price = product_variant.price
        
#         print(product_image,"))))))))))))))))))))))))))))))))))))))))))))")
#         print(product_description,"))))))))))))))))))))))))))))))))))))))))))))")
#         print(product_brand_image,"))))))))))))))))))))))))))))))))))))))))))))")
#         print(product_color,"))))))))))))))))))))))))))))))))))))))))))))")
#         print(product_size,"))))))))))))))))))))))))))))))))))))))))))))")
#         print(product_price,"))))))))))))))))))))))))))))))))))))))))))))")
        
#         subtotal = product_price * product_quantity
        
#         item = {
#            'product_quantity' : product_quantity,
#            'product_image' : product_image,
#            'product_description' : product_description,
#            'product_brand_image' : product_brand_image,
#            'product_color' : product_color,
#            'product_size' : product_size,
#            'product_price' : product_price,
#            'subtotal' : subtotal,
           
#        }
#         cart.append(item)
        
#         context = {
#             'cart': cart, 
#         }
  
#         return render(request,'user/cart.html',context)   
    
    
    
def add_cart_ajax(request):
    if request.method == "POST":
        color = request.POST.get('color')
        product = request.POST.get('product')
        user_id = request.POST.get('user_id')
        print(user_id,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        UserModel = get_user_model()
        user_instance = UserModel.objects.get(id=user_id)
        user_profile_instance = User_Profile.objects.get(user=user_instance)
   
       
        product = Product_variant.objects.filter(product__id=product,colors__code=color).first()
        
        print(product,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!+++++++++++++++++")
        if product:
            CartItem.objects.create(product_variant=product,customer=user_profile_instance)
            return JsonResponse(data={'message':'success'})
        return JsonResponse(data={'message':'product not get'})
    else:
        return JsonResponse({'error': 'Invalid request method'})


     
   
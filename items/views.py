from decimal import Decimal, InvalidOperation
from django.db.models import Q 
from functools import reduce
from tkinter import Image
from django.shortcuts import render,redirect, get_object_or_404
from items.models import Category
from .models import Brand, Color, Product_variant, ProductImage, Products ,Size

from django.contrib import messages

# Create your views here.


#CATAGORY_MANAGE-----------------------------------------------------------------------



def category_manage(request):
    category = Category.objects.all()
    print(category)
    context = {
        'category':category
    }
    return render(request,'admini/category_manage.html',context)


#ADD-CATAGORY---------------------------------------------------------------------------



def add_categories(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            category_name = request.POST.get('name')
            category_image = request.FILES.get('image')
            description = request.POST.get('description')
            print(description)
            # validating whether the field is empty
            
            if category_name.strip() == '':
                messages.error(request, 'field is empty!')
                return redirect('items:add_categories')
           
            # elif Category.objects.filter(name=category_name).exists():
            #     messages.error(request, 'The entered category is already taken')
            #     return redirect('items:add_categories')
            
            existing_category = Category.objects.filter(
                Q(name__iexact=category_name)
            ).first()

            if existing_category:
                messages.error(request, 'The entered category is already taken')
                return redirect('items:add_categories')
            
            elif not category_image:
                messages.error(request, 'image is not uploaded!')
                return redirect('items:add_categories')
            elif description.strip() == '':
                messages.error(request, 'description is not given!')
                return redirect('items:add_categories')
            
            else:
                new_category = Category.objects.create(name=category_name,image=category_image,category_description=description)
                
                new_category.save()
                messages.success(request, 'Categories are added successfully')
                return redirect('items:category_manage')
        else:
            return redirect('items:category_manage')
    else:
        return redirect('for_admin:ad_login')    
    


#EDIT-CATAGORY---------------------------------------------------------------------------
    
    
    
def edit_categories(request,category_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            category_name = request.POST.get('edit_name')
            category_image = request.FILES.get('edit_image')
            description = request.POST.get('edit_description')
            
            
             #---validate the form data-----

            if category_name.strip() == "":
                messages.error(request,"Field is empty!")
                return redirect('items:category_manage')
            
            existing_category = Category.objects.filter(
                Q(name__iexact=category_name)
            ).first()

            if existing_category:
                messages.error(request, 'The entered category is already taken')
                return redirect('items:add_categories')
            
            elif not category_image:
                messages.error(request, 'Image is not uploaded!')
                return redirect('items:category_manage')
            elif description.strip() == '':
                messages.error(request, 'Description is not given!')
                return redirect('items:category_manage')
    
            # Update the category instance
        
            update = get_object_or_404(Category,id=category_id)
            update.name = category_name
            update.image = category_image
            update.category_description = description
        
            update.save()
            messages.success(request, 'Category updated successfully')
            return redirect('items:category_manage')

    else:
        return redirect('for_admin:ad_login')


#DELETE-CATAGORY---------------------------------------------------------------------------



def delete_categories(request,category_id):
    if request.user.is_superuser:
        category = get_object_or_404(Category, id=category_id)
        category.delete()
        return redirect('items:category_manage')
    else:
        return redirect('for_admin:ad_login')
  
  
  
#BRAND----------------------------------------------------------------------------------  
  
    
def brand(request):
    brand = Brand.objects.all()
    
    context = {
        'brand':brand
    }
    return render(request,'admini/brand.html',context)
    
  

#ADD-BRAND---------------------------------------------------------------------------



def add_brand(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            brand_name   = request.POST.get('name')
            brand_image = request.FILES.get('image')
            # validating whether the field is empty
          
            if brand_name.strip() == '':
                messages.error(request, 'field is empty!')
                return redirect('items:add_brand')
            elif Brand.objects.filter(brand_name=brand_name).exists():
                messages.error(request, 'the brand is already taken')
                return redirect('items:add_brand')
            elif not brand_image:
                messages.error(request, 'image is not uploaded!')
                return redirect('items:add_brand')
            
            
            else:
                new_brand = Brand.objects.create(brand_name=brand_name,brand_image=brand_image)
                
                new_brand.save()
               
                print(brand_image)
                messages.success(request, 'Brands are added successfully')
                return redirect('items:brand')
        
    else:
        return redirect('for_admin:ad_login')    
       


#EDIT-BRAND---------------------------------------------------------------------------
       
       
       
def edit_brand(request,brand_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            brand_name = request.POST.get('edit_name')
            brand_image = request.FILES.get('edit_image')
            
            
            
            #---validate the form data-----

            if brand_name.strip() == "":
                messages.error(request,"Field is empty!")
                return redirect('items:brand')
            elif Brand.objects.filter(brand_name=brand_name).exclude(id=brand_id).exists():
                messages.error(request, 'The brand name is already taken')
                return redirect('items:brand')
            elif not brand_image:
                messages.error(request, 'Image is not uploaded!')
                return redirect('items:brand')
            
            # Update the brand instance
        
            update = get_object_or_404(Brand,id=brand_id)
            update.brand_name = brand_name
            update.brand_image = brand_image
            print(brand_name)
        
            update.save()
            messages.success(request, 'Brand updated successfully')
            return redirect('items:brand')
        else:
            return render(request,'items:brand')
    else:
        return redirect('for_admin:ad_login')
    
 
 
#DELETE-BRAND---------------------------------------------------------------------------
    
    
    
def delete_brand(request,brand_id):
    if request.user.is_superuser:
        brand = get_object_or_404(Brand, id=brand_id)
        brand.delete()
        return redirect('items:brand')
    else:
        return redirect('for_admin:ad_login')
    
   
#COLOR-----------------------------------------------------------------------------------   
   
   
    
def color(request):
    color = Color.objects.all()
    
    context = {
        'color':color
    }
    
    return render(request,'admini/color.html',context)



#ADD-COLOR-----------------------------------------------------------------------------------  
    

def add_color(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            color_name   = request.POST.get('name')
            # validating whether the field is empty
            
            if color_name.strip() == '':
                messages.error(request, 'field is empty!')
                return redirect('items:add_color')
            elif Color.objects.filter(name=color_name).exists():
                messages.error(request, 'the color is already taken')
                return redirect('items:color')
            
            
            
            else:
                new_color = Color.objects.create(name=color_name)
                
                new_color.save()
                messages.success(request, 'Colors are added successfully')
                return redirect('items:color')
    
        else:
            return render(request,'admini/color.html')
    else:
        return redirect('for_admin:ad_login')     
    
    
#EDIT-COLOR-----------------------------------------------------------------------------------    
    
    
    
def edit_color(request,color_id):
    if request.user.is_superuser:
        if request.method == 'POST':
            color_name = request.POST.get('edit_name')
            
            
            
            
            #---validate the form data-----

            if color_name.strip() == "":
                messages.error(request,"Field is empty!")
                return redirect('items:color')
            elif Color.objects.filter(name=color_name).exclude(id=color_id).exists():
                messages.error(request, 'The color is already taken')
                return redirect('items:color')

            
            
            # Update the brand instance
        
            update = get_object_or_404(Color,id=color_id)
            update.name = color_name
            
            update.save()
            messages.success(request, 'Color updated successfully')
            return redirect('items:color')

    else:
        return redirect('for_admin:ad_login')
    
 
 
#DELETE-COLOR-----------------------------------------------------------------------------------    
    
    
    
def delete_color(request,color_id):
    if request.user.is_superuser:
        color = get_object_or_404(Color, id=color_id)
        color.delete()
        return redirect('items:color')
    else:
        return redirect('for_admin:ad_login')
      

#SIZE-----------------------------------------------------------------------------------  



def size(request):
    size = Size.objects.all()
    print(size)
    context = {
        'size' : size
        
    }
    return render(request,'admini/size.html',context)




#ADD-SIZE-----------------------------------------------------------------------------------  



def add_size(request):
    if request.user.is_superuser:
        if request.method == 'POST' :
            size_name   = request.POST.get('name')
            
            # validating whether the field is empty
            
            if size_name.strip() == '':
                messages.error(request, 'field is empty!')
                return redirect('items:add_size')
            elif Size.objects.filter(name=size_name).exists():
                messages.error(request, 'This size is already taken')
                return redirect('items:size')
            
            
            
            else:
                new_size = Size.objects.create(name=size_name)
                
                new_size.save()
                messages.success(request, 'Sizes are added successfully')
                return redirect('items:size')
        else:
            # Render the form for a GET request
            return render(request, 'admini/size.html')
    else:
        return redirect('for_admin:ad_login')  
    
   
    
#EDIT-SIZE-----------------------------------------------------------------------------------  



def edit_size(request,id):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST.get('edit_name')
            
            
            #---validate the form data-----

            if name.strip() == "":
                messages.error(request,"Field is empty!")
                return redirect('items:size')
            elif Size.objects.filter(name=name).exclude(id=id).exists():
                messages.error(request, 'The size is already taken')
                return redirect('items:size')

            
            
            # Update the brand instance
        
            update = get_object_or_404(Size,id=id)
            update.name = name
            
            update.save()
            messages.success(request, 'Size updated successfully')
            return redirect('items:size')

    else:
        return redirect('for_admin:ad_login')
    
    
    
#DELETE-SIZE-----------------------------------------------------------------------------------      
    
    
def delete_size(request,id):
    if request.user.is_superuser:
        size = get_object_or_404(Size, id=id)
        size.delete()
        return redirect('items:size')
    else:
        return redirect('for_admin:ad_login')
    

# PRODUCT-MANAGE-----------------------------------------------------------------------------------------
    
    
def product_manage(request):
    products = Products.objects.all()
    category=Category.objects.all()
    brand=Brand.objects.all()
    for item in products:
        print(item.image.url)
    context={
        'product' :products,
        'brand':brand,
        'category':category,
        }
    return render(request,'admini/pro_manage.html',context)



# ADD-PRODUCT-----------------------------------------------------------------------------------------



def add_product(request):  
            
    if request.user.is_superuser:
        category=Category.objects.all()
        brand=Brand.objects.all()
    
        if request.method == "POST":
            name = request.POST['name']
            description = request.POST['description']
            product_image = request.FILES.get('image')
            brand_name = request.POST.get('brand')
            category_name = request.POST.get('category')
            
            if not product_image:
                messages.error(request, 'Image is not uploaded!')
                return redirect('items:product_manage')
            
            brand_instance = Brand.objects.get(brand_name = brand_name)
            category_instance = Category.objects.get(name = category_name)
            
            product = Products.objects.create(
                name = name,
                description = description,
                image = product_image,
                brand = brand_instance,
                category = category_instance,
            )
            product.save()
            messages.success(request, 'Product added successfully.')
            return redirect('items:product_manage')

        context={
            'brand':brand,
            'category':category,
           }
        return render(request, 'admini/product/add_pro.html',context)
 
    else:   
        return redirect('for_admin:ad_login')
    
    
 # EDIT-PRODUCT-----------------------------------------------------------------------------------------
   
    
def edit_product(request,product_id): 
    
    if request.user.is_superuser:

        
        if request.method == 'POST':
            name = request.POST.get('edit_name')
            description = request.POST.get('edit_description')
            product_image = request.FILES.get('edit_image')
            brand = request.POST.get('brand')
            category_name = request.POST.get('category')
            
            print(product_id, name, brand, category_name, description)
            
             #---validate the form data-----

            
      
            
             # Create an instance of Brand
            brand_instance = Brand.objects.get(brand_name=brand)
            print(brand,'brand')
             # Create an instance of category
            
            category_instance = Category.objects.get(id=category_name)
            
            update = get_object_or_404(Products,id=product_id)
            print(update, 'product')
            update.name = name
            update.description = description
            if product_image:
                update.image = product_image
            update.brand = brand_instance
            update.category = category_instance
        
            update.save()
            
            messages.success(request, 'Product updated successfully')
            return redirect('items:product_manage')
        
        
        

        return render(request, 'admini/pro_manage.html')
        
    else:

        return redirect('for_admin:ad_login')
    
   
# DELETE-PRODUCT-----------------------------------------------------------------------------------------
    
def delete_product(request, product_id):
    if request.user.is_superuser:
        product = get_object_or_404(Products, id=product_id)  # Use `product_id` here, not `id`
        product.delete()
        return redirect('items:product_manage')
    else:
        return redirect('for_admin:ad_login')
    
   

#VARIANT-----------------------------------------------------------------------------------  


def variant(request):
    variant = Product_variant.objects.all()
    colors = Color.objects.all()
    products = Products.objects.all()
    sizes = Size.objects.all()
    print(sizes)
    context = {
        'variant' : variant,
        'colors': colors,
        'products': products,
        'sizes': sizes,
        
    }
    return render(request,'admini/variant.html',context)


def add_variant(request):
    if request.user.is_superuser:
       
        if request.method == "POST":
            
            product_name = request.POST.get('product')
            price = request.POST['price']
            stock = request.POST.get('stock')
            images = request.FILES.getlist('images')
            
            selected_color_ids = request.POST.getlist('color')
            selected_size_ids = request.POST.getlist('size')
            
            # Validate the form data
            if not product_name:
                messages.error(request, 'Product name is required.')
            if not price:
                messages.error(request, 'Price is required.')
            if not selected_color_ids:
                messages.error(request, 'Select at least one color.')
            if not selected_size_ids:
                messages.error(request, 'Select at least one size.')

            # Check if there are any validation errors
            if messages.get_messages(request):
                return redirect('items:variant')  # Redirect back to the form page

            try:
                product_instance = Products.objects.get(name=product_name)
            except Products.DoesNotExist:
                # Handle the case when the product doesn't exist
                messages.error(request, 'Product does not exist.')
                return redirect('items:variant')

            
            
            
            product_variant = Product_variant.objects.create(
                        product=product_instance,
                        price=price,
                        stock=stock,
                    )
            for i in images:
                image=ProductImage(pro_variant= product_variant,images=i)
                image.save()
               
            
             # Add the selected colors and sizes to the many-to-many fields
            product_variant.colors.set(selected_color_ids)
            product_variant.size.set(selected_size_ids)
        
            product_variant.save()
            messages.success(request, 'Variant added successfully.')
            return redirect('items:variant')
    
    
    else:   
        return redirect('for_admin:ad_login')
    
    
    
        

def edit_variant(request, variant_id):
    if request.user.is_superuser:
        try:
            variant = Product_variant.objects.get(id=variant_id)
        except Product_variant.DoesNotExist:
            # Handle the case when the variant doesn't exist
            messages.error(request, 'Variant does not exist.')
            return redirect('items:variant')

        if request.method == 'POST':
            product_name = request.POST.get('product')
            price = request.POST['price']
            stock = request.POST.get('stock')
            selected_color_ids = request.POST.getlist('color')
            selected_size_ids = request.POST.getlist('size')

            # Validate the form data
            if not product_name:
                messages.error(request, 'Product name is required.')
            elif not price:
                messages.error(request, 'Price is required.')
            elif not selected_color_ids:
                messages.error(request, 'Select at least one color.')
            elif not selected_size_ids:
                messages.error(request, 'Select at least one size.')

            # Check if there are any validation errors
            if messages.get_messages(request):
                return redirect('items:edit_variant', variant_id=variant_id)

            try:
                product_instance = Products.objects.get(name=product_name)
            except Products.DoesNotExist:
                # Handle the case when the product doesn't exist
                messages.error(request, 'Product does not exist.')
                return redirect('items:edit_variant', variant_id=variant_id)

            # Update the variant fields
            variant.product = product_instance
            variant.price = price
            variant.stock = stock
            variant.colors.set(selected_color_ids)
            variant.size.set(selected_size_ids)

            variant.save()
            messages.success(request, 'Variant updated successfully.')
            return redirect('items:variant')

        # If it's a GET request, render the edit form
        colors = Color.objects.all()
        sizes = Size.objects.all()
        products = Products.objects.all()

        context = {
            'variant': variant,
            'colors': colors,
            'sizes': sizes,
            'products': products,
        }
        return render(request, 'admini/variant.html', context)

    else:
        return redirect('for_admin:ad_login')



def delete_variant(request,variant_id): 
    if request.user.is_superuser:
        variant = Product_variant.objects.get(id=variant_id)
        variant.delete()
        return redirect('items:variant')
    else:
        return redirect('for_admin:ad_login')
        
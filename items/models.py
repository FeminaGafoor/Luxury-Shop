from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField( max_length=255, blank=True, default="", null=True)
    image = models.ImageField( upload_to='images/',height_field=None, width_field=None, max_length=None,default=True)
    category_description = models.CharField( max_length=100, blank=True, default=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=50,blank=True,null=True)
    brand_image = models.ImageField( upload_to='brand_img/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    
    
    def __str__(self):
        return self.brand_name
    

class Color(models.Model):
    name = models.CharField(max_length= 50)
    
    
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length= 10)   
    
    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images/',blank=True)
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, blank=True,null=True, on_delete=models.SET_NULL,)
    create = models.DateTimeField(auto_now_add=True,null=True)
    update = models.DateTimeField(auto_now_add=True,null=True)

    
    
    def __str__(self):
        return self.name


    
class Product_variant(models.Model):
    product = models.ForeignKey(Products, blank=True, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    colors = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.CharField(max_length=100,blank=True)                         
    
    
    def __str__(self):
        return str(self.product)
       
       
class ProductImage(models.Model):
    
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    images = models.FileField(upload_to='variantproduct_images/',blank=True)
    
    def __str__(self):
        return str(self.pro_variant) 
    
    
class MutipleImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    images = models.FileField(null=True, blank=True)
    
    def __str__(self):
        return self.product.name
    
    


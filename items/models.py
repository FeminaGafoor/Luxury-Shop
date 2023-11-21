from django.db import models
from django.utils.safestring import mark_safe
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
    code= models.CharField(max_length=10,blank=True,null=True)
    
    
    def __str__(self):
        return self.name
    
    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p style="background-color:{}">Color </p>'.format(self.code))
        else:
            return ""

class Size(models.Model):
    name = models.CharField(max_length= 10)   
    
    def __str__(self):
        return self.name
    

class Products(models.Model):
    VARIANTS=(
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color','Size-Color'),
    )
    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='product_images/',blank=True)
    brand = models.ForeignKey(Brand, blank=True, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, blank=True,null=True, on_delete=models.SET_NULL,)
    create = models.DateTimeField(auto_now_add=True,null=True)
    update = models.DateTimeField(auto_now_add=True,null=True)
    variant=models.CharField(max_length=10,choices=VARIANTS,default='None')

        
    
    def __str__(self):
        return self.name
    
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url)) 
        else:
            return ""




    
class Product_variant(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    product = models.ForeignKey(Products, blank=True, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    colors = models.ManyToManyField(Color, blank=True)  
    size = models.ManyToManyField(Size, blank=True)  
    image_id = models.IntegerField(blank=True,null=True,default=0)
    stock = models.CharField(max_length=100,blank=True)                         
    
    
    def __str__(self):
        return str(self.product)
    
    
class MultipleImage(models.Model):
    product_variant = models.ForeignKey(Product_variant, on_delete=models.SET_NULL,blank =True, null=True)
    images=models.ImageField(upload_to='variantproduct_images',blank=True)
  

    def display_images(self):
        images_html = ""                
        for image in self.images.all():
            images_html += f'<img src="{image.url}" height="50" />'
        return mark_safe(images_html)
    
    def __str__(self):
        if self.product_variant:
            return f"{self.product_variant.product.name} - {self.pk}"
        return f"MultipleImage object ({self.pk})"


class Banner(models.Model):
    ban_image = models.ImageField(upload_to="banner_images", null=True, blank=True)
    fb_images = models.ImageField(upload_to="fb_images", null=True, blank=True)
    partners_images = models.ImageField(upload_to="partners_images", null=True, blank=True)
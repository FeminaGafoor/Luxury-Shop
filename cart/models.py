from django.db import models
from account.models import User_Profile
from items.models import Product_variant, Products
from django.utils import timezone
from django.contrib.auth.models import User

class Cart(models.Model):
    cart_id = models.CharField(max_length=250,blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id

class Cart_Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product = models.ForeignKey(Products,on_delete=models.CASCADE,blank=True,null=True)
    product_variant = models.ForeignKey(Product_variant,on_delete=models.SET_NULL,null=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.PositiveBigIntegerField(default=0)
    price = models.PositiveBigIntegerField(default=0)
    created_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    
    
    # @property
    # def sub_total(self):
    #     return self.product_variant.price*self.quantity
        

        



    

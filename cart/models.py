from django.db import models

from account.models import User_Profile
from items.models import Product_variant, Products

# Create your models here.


class CartItem(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)  
    customer = models.ForeignKey(User_Profile, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Products,on_delete=models.SET_NULL, null=True,blank = True)
    single_product = models.ForeignKey(Product_variant, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['date_added']

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"self.product.title"
    

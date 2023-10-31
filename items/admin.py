from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)
class ProductAdmin(admin.ModelAdmin):
    list_display =['id', 'name']
admin.site.register(Products, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Product_variant)
from django.contrib import admin
from .models import *
import admin_thumbnails
@admin_thumbnails.thumbnail('images')    
class ImageInlineAdmin(admin.TabularInline):
    model=MutipleImage
    readonly_fields=('id',)
    extra=1
    
class VariantInlineAdmin(admin.TabularInline):
    model=Product_variant
    readonly_fields=('image_tag',)
    extra=1    
    show_change_link=True
    
class ProductAdmin(admin.ModelAdmin):
    list_display =['name',]
    readonly_fields=('image_tag',)
    inlines=[ImageInlineAdmin,VariantInlineAdmin]
    
@admin_thumbnails.thumbnail('images')    
class ImageAdmin(admin.ModelAdmin):
    list_display=['title','images','id']    
    
class Product_variantAdmin(admin.ModelAdmin):
    list_display=['title','product','price','colors','size','image_id','stock','image_tag']
    
class ColorAdmin(admin.ModelAdmin):
    list_display=['name','code','color_tag']   
    
    
         
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color,ColorAdmin)
admin.site.register(Size)
admin.site.register(Products, ProductAdmin)
admin.site.register(Product_variant,Product_variantAdmin)
admin.site.register(MutipleImage,ImageAdmin)
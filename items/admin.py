from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.safestring import mark_safe

    
class ColorAdmin(admin.ModelAdmin):
    list_display=['name','code','color_tag']   
    
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('variant_id', 'product', 'price', 'get_colors', 'get_sizes', 'stock', 'display_image')

    def get_colors(self, obj):
        return ', '.join([color.name for color in obj.colors.all()])
    get_colors.short_description = 'Colors'

    def get_sizes(self, obj):
        return ', '.join([size.name for size in obj.size.all()])
    get_sizes.short_description = 'Sizes'

    # Add a method to display the Variant ID
    def variant_id(self, obj):
        return obj.id  # Replace 'id' with the actual field name representing the Variant ID
    variant_id.short_description = 'Variant ID'
    
   
    def display_image(self, obj):
        try:
            image = MultipleImage.objects.filter(product_variant=obj).first()
            if image:
                return format_html('<img src="{}" height="50" />', image.images.url)
        except MultipleImage.DoesNotExist:
            pass
        return ''
    display_image.allow_tags = True
    display_image.short_description = 'IMAGE'


         
# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color,ColorAdmin)
admin.site.register(Size)
admin.site.register(Products)
admin.site.register(Product_variant, ProductVariantAdmin)  


class MultipleImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'display_images')

    def display_images(self, obj):
        images_html = ""
        # Check if the image exists for the MultipleImage instance
        if obj.images:
            images_html += f'<img src="{obj.images.url}" height="50" />'
        return mark_safe(images_html)
    display_images.short_description = 'Images'  # Header for the column in the admin
    

admin.site.register(MultipleImage, MultipleImageAdmin)
admin.site.register(Banner)
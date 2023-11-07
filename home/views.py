from django.shortcuts import render

from items.models import Category
from items.models import Banner

# Create your views here.
def home(request):
    category_images = Category.objects.all().values('image')
    banner_images = Banner.objects.all()
    context = {
        'category_images': category_images,
        'banner_images' : banner_images
    }
    
    return render(request,'user/index.html',context)
    
    
  

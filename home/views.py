from django.shortcuts import render

from items.models import Category

# Create your views here.
def home(request):
    category_images = Category.objects.all().values('image')

    context = {
        'category_images': category_images
    }
    
    return render(request,'user/index.html',context)
    
    
  

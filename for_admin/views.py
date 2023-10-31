from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control


# Create your views here.

def ad_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
     
        
        # Authenticate user
        user_obj = authenticate(request, username=username, password=password)
        

        if user_obj is not None:
            if user_obj.is_superuser:
                # Login the user
                login(request, user_obj)
                return redirect('for_admin:admin_panel')
            else:
                messages.info(request, 'User is not a superuser.')
        else:
            messages.info(request, 'Invalid credentials.')

    # If not a POST request or authentication failed, render the login form
    return render(request, 'admini/ad_login.html')

    
@cache_control(no_store=True,no_cache=True)
@login_required(login_url='for_admin:ad_login')
def admin_panel(request):
    
    if not request.user.is_superuser:
        return render(request,'admini/ad_login.html')
    
    return render(request,'admini/index.html')



def ad_logout(request):
    
    logout(request)
    return render(request,'admini/ad_login.html')
    


def user_manage(request):
    user = User.objects.all()
    context = {
        'users':user
    }
    return render(request,'admini/user_manage.html',context )

def user_block(requset,user_id):
    
    #user is block
    user=User.objects.get(id = user_id)
    if user.is_active:
        user.is_active = False
        user.save()
    else:
        user.is_active = True
        user.save()
    return redirect('for_admin:user_manage')

    



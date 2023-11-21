import random
import re
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from account.models import Customer, User_Profile
from django.contrib import auth
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.views.decorators.cache import never_cache
from .models import User_Profile
from .forms import UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required



# Create your views here.



def register(request):
    if request.method == 'POST':
        
        #otp with signup----------
        
        get_otp = request.POST.get('otp')
        if get_otp:
            get_email = request.POST.get('email')
            user = Customer.objects.get('email = get_email')
            
            if not re.search(re.compile(r'^/{6}$'),get_otp):
                messages.error(request,'OTP should only contain numeric!')
                return render(request,'user/register.html',{'otp':True,'user':user})
            
            
            session_otp = request.session.get('otp')
            if int(get_otp) == session_otp:
                user.is_active = True
                user.save()
                auth.login(request,user)
                messages.success(request,f'Account is created for {user.username}')
       
                return redirect('account:user_login')
            else:
                messages.warning(request,f'you Entered a Wrong OTP')
 
                return render(request,'user/register.html',{'otp':True,'user':user})
 
        else:
            get_otp=request.POST.get('otp1')
            email=request.POST.get('user1')
        if get_otp:
            user=Customer.objects.get(email=email)
            messages.error(request,'field cannot empty!')
            return render(request,'user/register.html',{'otp':True,'user':user})
        else:
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password']
            repassword=request.POST['re_password']
          
            if username.strip() == '' or email.strip() == '' or   password.strip() == '' or repassword.strip() == '': 
                messages.info(request , ' field is empty!')
                return render(request, 'user/register.html')
            elif Customer.objects.filter(username=username).exists():
                messages.info(request, ' username is already taken')
                return render(request, 'user/register.html')
            elif Customer.objects.filter(email = email).exists():
                    messages.info(request, ' email is already taken')
                    return render(request, 'user/register.html')

            elif password != repassword:
                messages.info(request,'Invalid Password')
                return render(request, 'user/register.html')
            email_check = validator_email(email)
            if email_check is False:
                messages.info(request, 'email is not valid ')
                return render(request, 'user/register.html')
            password_check = validator_password(password)
            if password_check is False:
                messages.info(request, 'Please enter a strong password!')
                return render(request, 'user/register.html')
                
        if email_check and password_check:      
            # creating user
            new_user = Customer.objects.create_user(username=username , email= email , password=password )
          
            new_user.save()
            new_user.is_active=False
            new_user.last_login=None
            new_user.save()
            
            
              # Storing the user's email in the session
            request.session['user_email'] = email
            
            user_otp=random.randint(100000,999999)
            request.session['otp']=user_otp
            mess=f'Hello \t{new_user.username},\nOTP to verify your account for Luxury Shop  is {user_otp}\n Thanking You!'
            send_mail(
                    "Welcome to Luxury Shop, verify your Email",
                    mess,
                    settings.EMAIL_HOST_USER,
                    [new_user.email],

                    fail_silently=False
                )
            return redirect('account:verify_otp')
            # return render(request,'user/register.html',{'otp':True,'user':new_user})     
      

    return render(request,'user/register.html')
    
    
def validator_email(email):
    # Basic email format validation using a regular expression
    if re.match(r'^\S+@\S+\.\S+$', email):
        return True
    else:
        return False
    
    

def validator_password(password):
    # Password validation criteria (you can customize these)
    min_length = 6
    if len(password) < min_length:
        return False

    if not any(char.isupper() for char in password):
        return False

    if not any(char.islower() for char in password):
        return False

    if not any(char.isdigit() for char in password):
        return False
    
    return True

def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        session_otp = request.session.get('otp')
        user_email = request.session.get('user_email')  # Retrieve the user's email from the session

        if entered_otp and session_otp and entered_otp == str(session_otp):
            # OTP verification successful
            # Update the user's status to active
            try:
                user = Customer.objects.get(email=user_email)
                user.is_active = True
                user.save()
                auth.login(request, user)
                messages.success(request, f'Account is created for {user.username}')
                return redirect('account:user_login')
            except Customer.DoesNotExist:
                messages.error(request, 'User not found. Please try registering again.')
        else:
            # OTP verification failed
            messages.warning(request, 'You Entered a Wrong OTP')
            return render(request, 'user/otp.html', {'otp': True})
    return render(request, 'user/otp.html')




def user_login(request):
    if request.method == "POST":
        # Get the input values from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Try to retrieve a user based on either the username or email
        try:
            user = Customer.objects.get(Q(username=username) | Q(email=email))
        except Customer.DoesNotExist:
            user = None

        if user and check_password(password, user.password):
            # User found, and the password matches
            login(request, user)
            request.session['user'] = email
            # if user in request.session:
            return redirect('home:home')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('account:user_login')

    return render(request, 'user/login.html')


def user_logout(request):
    logout(request)
    return redirect('account:user_login')




def profile(request):
    
    if request.user.is_authenticated:
        user=request.user
        
      
        user_pro = User_Profile.objects.get(user=user)


        context = {
            
            'user_pro': user_pro,
        }
        return render(request, 'user/profile.html', context)
       
        
    return render(request, 'user/login.html')


# views.py

@login_required(login_url='user_login')
def edit_profile(request):
    try:
        # user_profile, created = User_Profile.objects.get_or_create(user=request.user)
        user_profile, created = User_Profile.objects.get_or_create(user=request.user)

    except User_Profile.DoesNotExist:
   
        user_profile = User_Profile(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()

            # Update the user's email
            user = request.user
            user.email = form.cleaned_data['email']
            user.save()

            messages.success(request, "Profile updated successfully!")
            return redirect('account:profile')
        else:
            messages.error(request, "Please correct the errors in the form.")
    
    else:
        form = UserProfileForm(instance=user_profile)

    context = {
        'form': form,
    }
    return render(request, 'user/edit_profile.html', context)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your Password was successfully updated!")
            return redirect('account:change_password')
        else:
            messages.error(request,'Please correct the error below.<br>'+ str(form.errors))
            return redirect('account:change_password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'user/change_password.html',{'form':form})
    
   
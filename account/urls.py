from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('user_login/',views.user_login,name='user_login'),
    path('register',views.register,name='register'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]
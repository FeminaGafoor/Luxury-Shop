from django.urls import path
from . import views

app_name='for_admin'    

urlpatterns = [
    path('ad_login/',views.ad_login,name='ad_login'),
    path('admin_panel/',views.admin_panel,name='admin_panel'),
    path('ad_logout/',views.ad_logout,name='ad_logout'),
    path('user_manage/',views.user_manage,name='user_manage'),
    path('user_block/<int:user_id>/',views.user_block,name='user_block'),
    
  
]
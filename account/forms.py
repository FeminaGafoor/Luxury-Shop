from django import forms
from .models import User_Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = ['user_name', 'first_name', 'last_name', 'phone','email','address', 'city', 'country', 'image']
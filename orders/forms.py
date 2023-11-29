from django import forms
from .models import Order


class Orderform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone','email','address_line_1','address_line_2','state', 'city', 'country','order_note']
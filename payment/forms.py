from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    Shipping_full_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Full Name'}),
        required=True
    )
    Shipping_email = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': ' Email'}),
        required=True
    )
        
    Shipping_adress1 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'آدرس اول'}),
        required=True
    )
    Shipping_adress2 = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'آدرس دوم'}),
        required=False
    )
    Shipping_city = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'شهر'}),
        required=True
    )
    Shipping_state = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'منطقه'}),
        required=False
    )
    Shipping_zipcode = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'کدپستی'}),
        required=False
    )
    Shipping_country = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'کشور'}),
        required=True
    )


    class Meta:
        model = ShippingAddress
        fields = [
            'Shipping_full_name',
            'Shipping_email', 
            'Shipping_adress1', 
            'Shipping_adress2', 
            'Shipping_city',
            'Shipping_state',
            'Shipping_zipcode', 
            'Shipping_country' 
        ]

        exclude = ['user',]

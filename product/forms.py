from django.forms import  Textarea, TextInput, IntegerField, ImageField, BooleanField, DateTimeField
from django import forms

from .models import Product, Category, Attribute, Variation, ProductImage 
from .models import LinkedProduct, Price, Inventory, Shipping

class ProductForm(forms.ModelForm):
	title = forms.CharField(
	    max_length=250,
	    label = 'Product Title',
	    widget=forms.NumberInput(attrs={
	        'class': 'form-control',
	        'placeholder': 'Product Title',
	        'title': 'Product Title',
	        # 'autocomplete': 'off',
	        'min':'1'
	    }),
	)
		
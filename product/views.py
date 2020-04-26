from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
# Create your views here.

def index(request,product_slug):
	product = Product.objects.get(slug=product_slug)
	context = {'product': product }
	return render(request, 'product/single_product.html', context)
from django.shortcuts import render
from django.http import HttpResponse
import json
import os
from OnlineShopping.settings import SITE_URL, FULL_MEDIA_URL
# from . import app_settings


# Create your views here.

from product.models import Product, Category

def index(request):
	# return HttpResponse("welcome")
	return render(request, 'index.html')


def shop_page(request):
	context = {'page_titile':'Shop Page'}
	try:
		products = Product.objects.all()
		categories = Category.objects.all()
		context.update( categories=categories, products=products,)
	except Exception as e:
		# raise e
		pass
	return render(request, 'shop_page.html', context)

def category_page(request, category_slug):
	context = {'page_titile':'Shop By Category',}
	try:
		category = Category.objects.get(slug=category_slug)
		context.update(category_name=category)
		products = Product.objects.all()
		# categories = Category.objects.all()
		categories =  get_categories()
		# print("test=", products)
		# print('test=', products)
		context.update( categories=categories, products=products,)
	except Exception as e:
		# raise e
		pass

	# cat_data = get_categories()
	# print('[++]', cat_data )
	return render(request, 'shop_page.html', context)

def get_categories(parent_id=True):
	cat_data = {}
	if type(parent_id) is bool:
		categories = Category.objects.filter(parent__isnull=parent_id)

	else:
		categories = Category.objects.filter(parent=parent_id)

	count = 0
	if categories:
		for category in categories:
			sub_cat = get_categories(category.id)
			
			if sub_cat:
				cat_data[category.name] = sub_cat
			else:
				cat_data[category.name] = []
	return cat_data


def sign_in(request):
	pass

def sign_out(request):
	pass

def register(request):
	pass

def sitemap(request):
	context= {'data': 'pranav',}
	# return HttpResponse("welcome")
	return render(request, 'sitemap.xml', context=context,   content_type = 'application/xml', )
	

def error_400(request, exception):
	context = {}
	return render(request, 'errors/404.html', context=context,   )

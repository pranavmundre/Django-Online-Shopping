from django.contrib import admin
from .models import Product, Category, Attribute, Variant

from django.utils.safestring import mark_safe
from django.utils.html import format_html

import math
from OnlineShopping.settings import SITE_URL
# Register your models here.

class Product_List(admin.ModelAdmin):
	list_display = ( 'get_image', 'title', 'price', 'sale_price', 'stock' , 'is_publish', 'updated_date', 'created_date')
	list_display_links = ( 'get_image', 'title',)
	list_filter = ('created_date' , 'is_publish',)
	# list_per_page = 10
	search_fields = ['title', 'price', 'sale_price',]
	ordering = ['-updated_date']
	# unique_together = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',), }

	# fields = (('title', 'slug'),  'description', 'image', 'is_publish')
	# actions = ('set_to_publish', 'set_to_unpublish')
	readonly_fields = ('preview_product',)

	def get_image(self, obj):
		# image = ''
		if obj.image:
			image = '<img src="'+SITE_URL+'/media/'+str(obj.image)+'" title="'+obj.title+'" alt="'+obj.title+'" height="40" />'
		else:
			image = '<img src="'+SITE_URL+'/media/product_image/default_product_image.png" title="'+obj.title+'" alt="'+obj.title+'" height="40" />'

		
		return mark_safe(image)

	def preview_product(self, obj):
		url = '<a href="'+SITE_URL+'/product/'+obj.slug+'" target="'+obj.slug+'" >'+SITE_URL+'/product/'+obj.slug+'/</a>' 
		return mark_safe(url)

	get_image.short_description = 'Image'

class Category_List(admin.ModelAdmin):
	list_display = ('name', 'get_slug')
	list_display_links = ('name', 'get_slug')
	prepopulated_fields = {'slug': ('name',), }
	# list_filter = ('category_name' , '',)

	def get_slug(self, obj):
		url = '<a href="'+SITE_URL+'/product/'+obj.slug+'" target="'+obj.slug+'" >'+SITE_URL+'product/'+obj.slug+'/</a>' 
		return mark_safe(url)

	get_slug.short_description = 'Slug'

# class Attribute_List(admin.ModelAdmin):
# 	pass
	 
		
class Variant_List(admin.ModelAdmin):
	list_display = ( 'get_variant', 'price')

	def get_variant(self, obj):
		data = ''
		variants =  obj.variant.all()
		for variant in variants:
			data = data + str(variant)+ ", "
		print("tesat", data)
		return data

admin.site.register(Product, Product_List)
admin.site.register(Attribute)
admin.site.register(Category, Category_List)
admin.site.register(Variant, Variant_List)
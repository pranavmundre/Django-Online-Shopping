from django.contrib import admin
from .models import Product, Category, Attribute, Variation, ProductImage 
from .models import LinkedProduct, Price, Inventory, Shipping

from django.utils.safestring import mark_safe
from django.utils.html import format_html

import math
from OnlineShopping.settings import SITE_URL, FULL_MEDIA_URL
# Register your models here.


class ProductImageAdmin(admin.TabularInline):
	model = ProductImage

# class VariationAdminTabular(admin.TabularInline):
# 	model = Variation

class LinkedProductAdminTabular(admin.TabularInline):
	model = LinkedProduct

class PriceAdmin(admin.TabularInline):
	model = Price

class ShippingAdmin(admin.TabularInline):
	model = Shipping

class InventoryAdmin(admin.TabularInline):
	model = Inventory

class ProductAdmin(admin.ModelAdmin):
	inlines = [ PriceAdmin, InventoryAdmin, ShippingAdmin, ProductImageAdmin,    LinkedProductAdminTabular ]
	list_display = ( 'get_featured_image', 'title' , 'get_category' , 'is_publish', 'updated_date', 'created_date')
	# list_display = ( 'get_featured_image', 'title', 'price', 'sale_price', 'stock_quantity' , 'get_category' , 'is_publish', 'updated_date', 'created_date')
	list_display_links = ( 'get_featured_image', 'title',)
	list_filter = ('category' , 'is_publish',)
	# list_per_page = 10
	# search_fields = ['title', 'price', 'sale_price',]
	ordering = ['-updated_date']
	# unique_together = ('title', 'slug')
	prepopulated_fields = {'slug': ('title',), }

	# fields = (('title', 'slug'),  'description', 'image', 'is_publish')
	# actions = ('set_to_publish', 'set_to_unpublish')
	readonly_fields = ('preview_product',)

	def get_featured_image(self, obj):
		# image = ''
		if obj.featured_image:
			image = '<img src="'+FULL_MEDIA_URL+str(obj.featured_image)+'" title="'+obj.title+'" alt="" height="40" />'
		else:
			image = '<img src="'+FULL_MEDIA_URL+'product_image/default_product_image.png" title="'+obj.title+'" alt="" height="40" />'

		# image_r = obj.featured_image
		# return image_r
		return mark_safe(image)

	def preview_product(self, obj):
		url = '<a href="'+SITE_URL+'/product/'+obj.slug+'" target="'+obj.slug+'" >'+SITE_URL+'/product/'+obj.slug+'/</a>' 
		return mark_safe(url)

	def get_category(self, obj):
		data = ''
		categories =  obj.category.all()
		for category in categories:
			data = data + str(category)+ ", "
		return data

	get_featured_image.short_description = 'Image'
	get_category.short_description = 'Category'

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('get_name', 'get_slug')
	list_display_links = ('get_name', 'get_slug')
	prepopulated_fields = {'slug': ('name',), }
	# list_filter = ('category_name' , '',)

	def get_slug(self, obj):
		url = '<a href="'+SITE_URL+'/product/'+obj.slug+'" target="'+obj.slug+'" >'+SITE_URL+'/product/'+obj.slug+'/</a>' 
		return mark_safe(url)

	def get_name(self, obj):
		
		if obj.parent:
			cat_data = Category.objects.get(id=obj.parent_id)
			cat = str(obj.name)+ '-->'+str(cat_data.name)
		else:
			cat = obj.name


		return cat 

	get_slug.short_description = 'Slug'
	get_name.short_description = 'Category'

# class AttributeAdmin(admin.ModelAdmin):
# 	pass
	 
		
class VariationAdmin(admin.ModelAdmin):
	# list_display = ( 'get_variation', 'price')

	def get_variation(self, obj):
		data = ''
		variations =  obj.variation.all()
		for variation in variations:
			data = data + str(variation)+ ", "
		# print("tesat", data)
		return data



	 # pass
		
admin.site.register(Product, ProductAdmin)
admin.site.register(Attribute)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Variation)
admin.site.register(Price)

# admin.site.register(ProductImage)
# admin.site.register(ProductImage, ProductImageAdmin)
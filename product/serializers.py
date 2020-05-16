from OnlineShopping.settings import SITE_URL, FULL_MEDIA_URL

from rest_framework.serializers import ModelSerializer, ReadOnlyField, DecimalField, DateTimeField
from rest_framework import serializers
from .models import Product, Category, Attribute, Variation, ProductImage 
from .models import LinkedProduct, Price, Inventory, Shipping


class CategorySerializer(serializers.RelatedField):
	class Meta:
		model = Category

	def to_representation(self, value):
         return value.name

class ShippingSerializer(serializers.RelatedField):
	class Meta:
		model = Shipping
		fields = ('height')


class PriceSerializer(serializers.RelatedField):
	class Meta:
		model = Price

	def to_representation(self, instance):
		data = super().to_representation(instance)
		data['regular_price'] = instance.regular_price 
		return data

class ProductSerializer(serializers.ModelSerializer):
	title = serializers.CharField()
	slug = serializers.SlugField()
	created_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
	updated_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
	featured_image = serializers.SerializerMethodField('get_featured_image_url')
	category = CategorySerializer( read_only=True, many=True)
	
	regular_price = DecimalField(source='price.regular_price', read_only=True, decimal_places=2 , max_digits=100, )
	sale_price = DecimalField(source='price.sale_price', read_only=True, decimal_places=2 , max_digits=100, )
	sale_start_date = DateTimeField(source='price.sale_start_date' )
	sale_end_date = DateTimeField(source='price.sale_end_date' )

	class Meta:
		model = Product
		fields = ('__all__')
		depth = 1
		# fields = ('id', 'title', 'slug', 'category')

	# def get_single_product(self, object):
	# 	pass

	def get_category(self, object):
		category = object.category
		print('Test = ',category)
		return category

	def get_featured_image_url(self, object ):
		image_url = FULL_MEDIA_URL+str(object.featured_image)
		return image_url

# p = ProductSerializer(Product)
# p.data

	
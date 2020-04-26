from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=120 )
	slug = models.SlugField(unique=True)

	description  = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to='product_image/%Y/%m/%d', null=True, blank=True)
	price  = models.DecimalField(decimal_places=2 , max_digits=100, )
	sale_price  = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
	stock = models.PositiveIntegerField()
	product_category = models.ManyToManyField('Category', )

	allow_variants = models.BooleanField(default=False)
	product_variants = models.ManyToManyField( 'Attribute', related_name='product_attribute' )

	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_date = models.DateTimeField(auto_now_add =False ,auto_now=True)
	is_publish = models.BooleanField(default=True) 
	
	class Meta:
		db_table = "products"

	def __str__(self):
		return self.title

	def get_price(self):
		if self.price > self.sale_price :
			price = self.sale_price
		else:
			price = self.price
		return price



class Category(models.Model):
	# parent_id = models.CharField( max_length=120,  blank=True, null=True )
	category_name = models.CharField(max_length=120, unique=True)

	def __str__(self):
		return self.category_name


class Attribute(models.Model):
	"""
	This model holds the attr_type (ex: color) and attribute_name (ex: red)
	"""
	product = models.ForeignKey('Product', on_delete=models.CASCADE,  )
	# attribute_type = models.ForeignKey( 'Variant', on_delete=models.PROTECT , blank=True, null=True)
	attribute_name = models.CharField(max_length=155, blank=True)

	def __str__(self):
		return self.attribute_name

class Variant(models.Model):
	"""
	This model holds the values for price and combination of attributes
	"""
	product = models.ForeignKey('Product', on_delete=models.CASCADE,   )
	variant = models.ManyToManyField( 'Attribute', )
	sku = models.CharField(max_length=155, blank=True)
	price = models.DecimalField(max_digits=25, decimal_places=2)

	# def __str__(self):
	# 	return self.variant


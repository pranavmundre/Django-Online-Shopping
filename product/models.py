from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator , MaxValueValidator


# Create your models here.

'''
def validate_image(image):
    file_size = image.file.size
    # limit_kb = 150
    # if file_size > limit_kb * 1024:
    #     raise ValidationError("Max size of file is %s KB" % limit)

    limit_mb = 2
    if file_size > limit_mb * 1024 * 1024:
       raise ValidationError("Max size of file is %s MB" % limit_mb)

'''
class Product(models.Model):
	PRODUCT_TYPE = (
			('simple_product', 'Simple Product'),
			('variable_product', 'Variable Product')
		)

	title = models.CharField(max_length=120 )
	slug = models.SlugField(unique=True)
	short_description  = models.TextField( max_length=100 ,null=True, blank=True)
	description  = models.TextField(null=True, blank=True)
	featured_image = models.ImageField(upload_to='product_image/%Y/%m/%d', default='product_image/default_product_image.png',verbose_name = 'Product Image' , null=True, blank=True, )
	# featured_image = models.ImageField(upload_to='product_image/%Y/%m/%d', default='product_image/default_product_image.png',verbose_name = 'Product Image' , null=True, blank=True, validators=[validate_image])
	category = models.ManyToManyField('Category',  blank=True, related_name='category' )

	product_type = models.CharField(max_length=18, choices=PRODUCT_TYPE, default='simple_product' )

	# Inventory
	# inventory = models.OneToOneField( 'Inventory', related_name='inventory_data', on_delete=models.CASCADE,)
	
	#Shipping
	# shipping = models.OneToOneField( 'Shipping', related_name='Shipping_data', on_delete=models.CASCADE, null=True, blank=True)

	created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_date = models.DateTimeField(auto_now_add =False ,auto_now=True)
	is_publish = models.BooleanField(default=True) 
	
	class Meta:
		db_table = "products"

	class Media:
		js = '/admin/js/custom.js'

	def __str__(self):
		return self.title

	@property
	def thumbnail(self):
		if self.featured_image:
			return get_thumbnail(self.featured_image, '50x50', quality=90)
		return None

class Price(models.Model):
	product = models.OneToOneField('Product', on_delete=models.CASCADE,  )
	regular_price = models.DecimalField(decimal_places=2 , max_digits=100, validators=[MinValueValidator(0)], null=True, blank=True,)
	sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True, validators=[MinValueValidator(0)])
	sale_start_date = models.DateTimeField(null=True, blank=True, )
	sale_end_date = models.DateTimeField(null=True, blank=True, )
	
	def get_price(self):
		if self.regular_price > self.sale_price :
			price = self.sale_price
		else:
			price = self.regular_price
		return price


class ProductImage(models.Model):
	product = models.ForeignKey('Product', on_delete=models.CASCADE,  )
	images = models.ImageField(upload_to='product_image/%Y/%m/%d' , null=True, blank=True)

	# def __str__(self):
	# 	return self.image
		
class Category(models.Model):
	name = models.CharField(max_length=120, unique=False)
	slug = models.SlugField(unique=True)
	parent = models.ForeignKey('self', on_delete=models.CASCADE,  related_name='parent_category',  null=True, default=0 , blank=True,  )

	def __str__(self):
		return self.name

	@property
	def category_name(self):
		return self.category.name

	@property
	def get_category_slug(self):
		return self.category.slug


class Attribute(models.Model):
	"""
	This model holds the attr_type (ex: color) and attribute_name (ex: red)
	"""
	product = models.ForeignKey('Product', on_delete=models.CASCADE, blank=True, null=True  )
	visible_on_product_page = models.BooleanField(default=False) 
	used_for_variation = models.BooleanField(default=False) 
	attribute_name = models.CharField(max_length=155, unique=True)
	attribute_value = models.CharField(max_length=155, unique=False,  )

	# class Meta:
	# 	unique_together	= ['attribute_name', 'attribute_value']

	def __str__(self):
		return self.attribute_name

class Variation(models.Model):
	"""	This model holds the values for price and combination of attributes """
	product = models.ForeignKey('Product', on_delete=models.CASCADE,   )
	type = models.ForeignKey( 'Attribute', on_delete=models.CASCADE, )
	value = models.CharField(max_length=155,)
	price = models.OneToOneField( 'Price', related_name='price_data', on_delete=models.CASCADE,)
	
	inventory = models.OneToOneField( 'Inventory', related_name='Inventory_data', on_delete=models.CASCADE,)
	shipping = models.OneToOneField( 'Shipping', related_name='shipping_data', on_delete=models.CASCADE,)
	description  = models.TextField(null=True, blank=True)

	class Meta:
		unique_together = (('product', 'type', 'value'),)

	# def __str__(self):
	# 	return self.Variation

class LinkedProduct(models.Model):
	product = models.OneToOneField('Product', on_delete=models.CASCADE,   )
	up_sell = models.ManyToManyField('Product', related_name='up_sell',  blank=True )
	cross_sell = models.ManyToManyField('Product', related_name='cross_sell',  blank=True )

class Inventory(models.Model):
	product = models.OneToOneField('Product', on_delete=models.CASCADE,   )
	STOCK_STUTUS = (
		('in_stock', 'In stock'),
		('out_of_stock', 'Out of stock'),
		('on_backorder', 'On backorder'),
	)
	ALLOW_BACKORDER = (
			('do_not_allow', 'Do not allow'),
			('allow_but_notify', 'Allow, but notify customer'),
			('allow', 'Allow'),
		)
	
	sku = models.CharField(max_length=50,  null=True, blank=True, )
	manage_stock =  models.BooleanField(default=False) 
	stock_quantity = models.IntegerField( null=True, blank=True,)
	allow_backorders = models.CharField(max_length=20, choices=ALLOW_BACKORDER, blank=True, help_text='If managing stock, this controls whether or not backorders are allowed. If enabled, stock quantity can go below 0.')
	stock_status = models.CharField(max_length=20, choices=STOCK_STUTUS, blank=True )
	sold_individually =  models.BooleanField(default=False) 
	
class Shipping(models.Model):
	product = models.OneToOneField('Product', on_delete=models.CASCADE,   related_name='single_product'  )
	weight = models.DecimalField(max_digits=25, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True, )
	length = models.DecimalField(max_digits=25, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True, )
	width = models.DecimalField(max_digits=25, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True, )
	height = models.DecimalField(max_digits=25, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True, )
	
	shipping_class = models.OneToOneField( 'ShippingClass', related_name='shipping_class_data', on_delete=models.CASCADE, null=True, blank=True)


"""
# SETTING FOR OUR STORE 
"""

class ShippingClass(models.Model):
	pass
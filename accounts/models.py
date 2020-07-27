from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from django.utils import timezone

from sorl.thumbnail import get_thumbnail 
from django.utils.safestring import mark_safe
# from django.utils.html import format_html
from OnlineShopping.settings import SITE_URL, FULL_MEDIA_URL

# Create your models here.


# class UserProfileManager(BaseUserManager):
# 	"""Help Django work with our custom user model"""
# 	def create_user(self, email='', password=None, first_name=None, last_name=None):
# 		"""Create user"""

# 		if not email:
# 			raise ValueError("Email required.")
		
# 		email = self.normalize_email(email)
# 		user = self.model(email=email, first_name=first_name, last_name=last_name )
		
# 		user.set_password(password)
# 		user.save()
# 		return user

# class UserProfile(AbstractBaseUser, PermissionsMixin):
# 	"""Represent user profile inside our system."""

# 	email = models.EmailField(max_length=255, unique=True)
# 	first_name = models.CharField(max_length=255, blank=True)
# 	last_name = models.CharField(max_length=255, blank=True)
# 	is_active = models.BooleanField(default=True)
# 	is_staff = models.BooleanField(default=False)

# 	# user = models.OneToOneField( User , on_delete=models.CASCADE)
# 	# phone_number = models.IntegerField(blank=True)

# 	objects = UserProfileManager()

# 	USERNAME_FIELD ='email'
# 	# REQUIRED_FIELD = ['']

# 	def get_full_name(self):
# 		""" Get the full name of user """
# 		return str(self.first_name)+" "+str(self.last_name)
# 	def get_short_name(self):
# 		"""Get the short name of user"""
# 		return self.first_name

# 	def __str__(self):
# 		"""Django used this when it need to convert the object string."""
# 		return self.email


GENDER = (
	( 'm' , 'Male'),
	( 'f' , 'Female'),
	( 'o' , 'Other'),
)
class UserProfile(models.Model):
	user = models.OneToOneField(User , on_delete=models.CASCADE, related_name="profile")
	birth_date = models.DateField(null=True, blank=True)
	mobile_no = models.CharField(null=True, blank=True,max_length=15, )
	gender = models.CharField( max_length=1, choices = GENDER, null=True, blank=True,)
	address = models.CharField( max_length=100, null=True, blank=True,)
	profile_image = models.ImageField(default='images/default-avtar.png', upload_to='users/%Y/%m/%d/', null=True, blank=True)

	is_student = models.BooleanField(default=False)

	objects = UserManager()

	def __str__(self):
		return self.user.username	

	# class Meta:
	# 	db_table = "user_profile"
	# @classmethod
	# def create_user(self, new_user_data):
	# 	"""Create user"""

	# 	if not  new_user_data['email'] :
	# 		raise ValueError("Email required.")
		
	# 	user = self.model(
	# 			email = new_user_data[email], 
	# 			username = new_user_data[email], 
	# 			first_name = new_user_data[first_name], 
	# 			last_name = new_user_data[last_name] 
	# 		)
		
	# 	# user.set_password(password)
	# 	user.save()
	# 	return user

	# @property
	def get_full_name(self):
		if self.user.first_name or self.user.last_name:
			return str(self.user.first_name)+" "+str(self.user.last_name)
		return "-"
	get_full_name.short_description = 'Full name'

	def get_profile_image(self):
		# image = ''
		if self.profile_image:
			thumb_url = get_thumbnail(self.profile_image, '40x40', crop='center', quality=60)
			image = '<img src="'+FULL_MEDIA_URL+str(thumb_url)+'" title="'+self.user.first_name+'" alt="" height="40" />'
		else:
			image = '<img src="'+FULL_MEDIA_URL+'images/default_avtar.png" title="'+self.user.first_name+'" alt="" height="40" />'

		# image_r = self.profile_image
		# return image_r
		return mark_safe(image)

	def profile_image_200x200(self):
		if self.profile_image:
			thumb_url = get_thumbnail(self.profile_image, '200x200', crop='center', quality=60)
			thumb_url= FULL_MEDIA_URL+str(thumb_url)
		else:
			thumb_url = 'images/default_avtar.png'
		return str(thumb_url)
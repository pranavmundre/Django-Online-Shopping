from django.contrib import admin
from .models import UserProfile
# Register your models here.




class UserProfileAdmin(admin.ModelAdmin):
	list_display = ( 'get_profile_image', 'user','get_full_name' , 'mobile_no', 'gender')
	list_display_links = ('user',)

	 
	
		
admin.site.register(UserProfile, UserProfileAdmin)
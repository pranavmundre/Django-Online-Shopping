from rest_framework import serializers, fields
from django.contrib.auth.models import User
from rest_framework import generics
from django.db import models

from accounts.models import UserProfile

from rest_framework.exceptions import ValidationError

from django.core.exceptions import ObjectDoesNotExist


# class UserSerializer(serializers.ModelSerializer):
# 	password = serializers.CharField(write_only=True)

# 	class Meta:
# 		model = User
# 		fields = ('first_name', 'last_name', 'email', 'username', 'password')
# 		# read_only_fields = ( 'email', 'password', 'username')

# 	def create(self, validated_data):
# 		user = super(UserSerializer, self).create(validated_data)
# 		user.set_password(validated_data['password'])
# 		user.save()
# 		return user


# class UserProfileSerializer(serializers.ModelSerializer):
# 	user = UserSerializer()
	
# 	class Meta:
# 		model = UserProfile
# 		fields = ('__all__')

# 	# def create(self, **validated_data):
# 	# 	return str(**validated_data.pop("email"))+ " ok"

# 	def is_valid(self, *arg, **kwarg):
# 		print("test=", self.data )
# 		# print("test=", self.data['first_name'] )
# 		# if not self.data["mobile_no"] :
# 			# raise ValidationError({'mobile_no': ['this field is not valid']})
# 		return True

# 	def create_user(self, *arg, **kwarg):
# 		user = User.objects.get(username=self.data.get("username"))
# 		profile = UserProfile.objects.create(
# 			user=user,
# 			mobile_no=self.data.get("mobile_no"),
# 			gender=self.data.get("gender"),
# 		);

# 		profile_data = {
# 			"mobile_no": profile.mobile_no,
# 			"gender": profile.gender,
# 		}
# 		return profile_data

# 	# def data(self, *arg):
# # 	return "ok"
# 	def update(self, instance, validated_data):
# 		user = User.objects.get(id=instance)
# 		user.first_name = validated_data['first_name'] if  validated_data['first_name'] else user.first_name 
# 		user.last_name = validated_data['last_name'] if  validated_data['last_name'] else user.last_name 
# 		user.save()

# 		user_pro = UserProfile.objects.get(user= user)
# 		user_pro.mobile_no = validated_data['mobile_no'] if  validated_data['mobile_no'] else user_pro.mobile_no 
# 		user_pro.save()

# 		validated_data['first_name'] = user.first_name
# 		validated_data['last_name'] = user.last_name
# 		validated_data['mobile_no'] = user_pro.mobile_no
# 		validated_data['gender'] = user_pro.gender

# 		return validated_data


 

	


class UserProfileSerializer(serializers.ModelSerializer):
	# birth_date = fields.DateField(input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
	# birth_date = fields.DateField()
	class Meta:
		model = UserProfile
		depth = 1
		# fields = ('__all__')
		fields = (
				'mobile_no',
				'gender', 
				'birth_date', 
				'profile_image', 
				'profile_image_200x200',
				'is_student'
			)
		read_only_fields = ( 'is_student',)
	

		

from rest_framework.parsers import FileUploadParser	
class UserSerializer(serializers.ModelSerializer):
	profile = UserProfileSerializer()
	# profile = serializers.HyperlinkedRelatedField(many=True)
	
	# parser_class = (FileUploadParser,)
	
	class Meta:
		model = User
		depth = 1
		fields = ( 'id', 'username', 'first_name', 'last_name', 'password','email' , 'profile' )
		read_only_fields = ( 'id', 'username',  )
		extra_kwargs = {'password': {'write_only': True, 'required': False, }}


	def create(self, validated_data):
		password = validated_data.pop('password')
		profile = validated_data.pop('profile')
		# print("create:", profile)

		try:
			user = User.objects.create(
					# username = validated_data.get('username'),
					username = validated_data.get('email'),
					email = validated_data.get('email'),
					first_name = validated_data.get('first_name'),
					last_name = validated_data.get('last_name'),
				)
			user.set_password(password)
			user.save()
		except Exception as e:
			# raise 
			return {'detail': 'user already exist.'}

		UserProfile.objects.create(user=user, **profile)
		return user

	def update(self, instance, validated_data):
		# print("update", validated_data)
		try:
			profile_data = validated_data.pop('profile')

			instance.email = validated_data.get('email', instance.email)
			instance.first_name = validated_data.get('first_name', instance.first_name)
			instance.last_name = validated_data.get('last_name', instance.last_name)
			instance.username = validated_data.get('username', instance.username)

			# password = validated_data.get('password', False)
			# if password:
			# 	print("ok:", password)
			# 	instance.set_password(password)

			instance.save()

			profile = instance.profile
			profile.mobile_no = profile_data.get('mobile_no', profile.mobile_no)
			profile.birth_date = profile_data.get('birth_date', profile.birth_date)
			profile.profile_image = profile_data.get('profile_image', profile.profile_image)
			profile.gender = profile_data.get('gender', profile.gender)
			profile.save()

		except ObjectDoesNotExist :
			profile = UserProfile.objects.create(
					user=instance,
					mobile_no=validated_data.get('mobile_no', ""),
					birth_date=validated_data.get('birth_date', None),
					gender=validated_data.get('gender', ""),
					profile_image=validated_data.get('profile_image', "images/default-avtar.png"),
				)
			# instance.push(profile)
			# return {
			# 	'status': instance.username,
			# 	'profile':profile
			# }
		except Exception as e:
			print("Exception", type(e))
			raise e
			pass

		return instance
			
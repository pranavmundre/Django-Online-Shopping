from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes

from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser,FormParser, JSONParser , MultiPartParser

from django.core import serializers
from django.utils.decorators import method_decorator 
from django.contrib.auth.decorators import login_required 

from django.http import Http404
from django.contrib.auth.models import User

from .serializers import UserSerializer
from .serializers import UserProfileSerializer 

from accounts.models import UserProfile
from OnlineShopping.settings import SITE_URL, FULL_MEDIA_URL

import json
# @api_view(['GET', 'POST', 'PUT'])
# def index(request):

# 	# user = User.objects.all()
# 	# s_d = UserSerializer(user, many=True)
# 	if request.method == 'GET':
# 		user_data = User.objects.all()
# 		print('Test=', user_data)
# 		serializer = UserSerializer(user_data, many=True)
# 		return Response(serializer.data, status=200)

# 	if request.method == 'POST' :
# 		user_data = UserProfileSerializer(data=request.data)
# 		print('Test=', request.data)

# 		if user_data.is_valid() :
# 			user_data.save(phone_number=request.phone_number)
# 			print('Test=add', request.data)
# 		else:
# 			return Response('Invaild Data', status=201)


# 	return Response('Not Found', status=400)



# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @method_decorator(login_required)
# @permission_classes([IsAuthenticated])
# @api_view(['GET', 'POST', 'PUT'])
# def test(request):
# 	context = {}
# 	user_data = {}
# 	user_data = UserProfile.objects.all()
# 	# user_data = serializers.serialize('json', User.objects.all(), fields=('__all__',))
# 	# serializer = UserProfileSerializer(user_data` , many=True)
# 	# for user in user_data:
# 	# 	print('Test: ',user.user.email)
# 	new_user ={
# 		'email': 'resr@gmai.com',
# 		'username': 'resr@gmai.com',
# 		'password': 'resr@gmai.com',
# 	}
# 	# user_obj = User.objects.create_user(username='resr@gmai.com')
# 	return Response(" serializers.serialize('json', iter(user_obj) )" , status=200)
# 	# return Response('user_data' , status=200)


class HelloView(APIView):
	# permission_classes = [IsAuthenticated, ]             # <-- And here
	# authentication_classes = [SessionAuthentication, BasicAuthentication]
	def get(self, request):

		# user = User.objects.get(username='pranav')
		# name= user.profile.gender
		content = {
				'message': 'Hello, World!',
				# 'data': name
			}
		# print("Test: ", request.user.profile.mobile_no)
		return Response(content)



class UserCreate(generics.CreateAPIView):
	# queryset = UserProfile.objects.all()
	# serializer_class = UserProfileSerializer
	serializer_class = UserSerializer
	permission_classes = (AllowAny, )
	# lookup_field = 'pk'
	page_size=2

	def post(self, request):
		context = {}
		user = {
			"username": request.data.get('username', None ),
			"email": 	request.data.get('email', None ),
			"password": request.data.get('password', None ),
		}
		user_profile = {
			"username": 	request.data.get("username", None ),
			"mobile_no": 	request.data.get("mobile_no", None ),
			"gender": 		request.data.get("gender", None ),
		}
		serialized_user = UserSerializer(data = user)
		serialized_profile = UserProfileSerializer(data = user_profile)
		
		if serialized_user.is_valid() & serialized_profile.is_valid():
			res_user = serialized_user.save()
			res_user_profile = serialized_profile.create_user()
			context = serialized_user.data
			context.update(  res_user_profile)
			return Response( context , status=status.HTTP_201_CREATED)
		else:
			if serialized_user.errors :
				return Response( serialized_user.errors , status=400)
			if serialized_profile.errors:
				return Response( serialized_profile.errors , status=400)

		return Response("post")
 

	def put(self, request):
		# serialized = UserProfile()
		# print("Test passed",request.data)
		# user = User.objects.all();
		
		serializer = UserSerializer(  data = request.data)
		try:
			serializer.is_valid()
			serializer.create();
			return Response(serializer.data, status=status.HTTP_200_OK)
		except  Exception as e:
		# 	raise e
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		# try:
		# 	print("Test2 passed", serialized)
		# 	# serialized.is_valid(raise_exception=True)
		# 	print("Test3 passed", serialized)
		# 	serialized.save()
		# 	return Response(serialized.errors, status=200)
		# except Exception as e:
		# 	raise e
		# 	return Response(serialized.data, status=200)
			# serialized.validated_data
		
		return Response({"msg": 'failed'}, status=404)

from .permissions import IsStudent

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	# lookup_field = 'id'
	parser_class = (FileUploadParser,)
	search_field = ("username", )
	# media_type = 'image/*'


	permission_classes = (IsAuthenticated,AllowAny, IsAdminUser, IsStudent )
	permission_classes_by_action = {
			 'create': (permissions.AllowAny,),
			'list': (permissions.IsAuthenticated),
	# 		'retrieve': (permissions.AllowAny,),
	# 		'update': (permissions.IsAuthenticated,),
	# 		'destroy': (permissions.IsAdminUser,),
	# 		'search': (permissions.IsAuthenticated,)  # <--- Option 1
		}

	# def get_queryset(self):
	# 	return self.queryset.filter(id=1)
	# def get_object(self, request):
	# 	obj = self.get(user=request.user)
	# 	return obj

	def create(self, request):
		serialized = UserSerializer(data=request.data)
		if serialized.is_valid():
			serialized.save()
			print("TEst:", serialized)
			return Response({'status': serialized.data}, status=201)
		else:
			return Response({'error': serialized.errors}, status=400)

 


class UploadProfilePicture(APIView):
	parser_class = (FileUploadParser,)
	media_type = 'image/*'
	
	def get(self, request, user_id,  pk=None):
		try:
			user = UserProfile.objects.get(user=user_id)
		except UserProfile.DoesNotExist :
			raise Http404
			# return Response( {'detail': 'invaild user.'} ,status=400)

		serialized = UserProfileSerializer(user, request.data)
		if serialized.is_valid() :
			serialized.save()
			print("File:", serialized.data)
			return Response( {'profile_image': SITE_URL + serialized.data['profile_image']} ,status=200)
			# return Response( {'profile_image': FULL_MEDIA_URL + str(user.profile_image)} ,status=status.HTTP_201_CREATED)
		else:
			return Response( serialized.errors ,status=400)

	 
class UserProfileUpdate(generics.UpdateAPIView):
	# user = User.objects.get(id=1)
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer
	# permission_classes = (IsAuthenticated,)
	# permission_classes = (AllowAny, )



	def get(self, request, user_id):
		# if self.request.user.id != user_id:
		# 	return Response({'details': 'Request Modified.'}, status=401)
		
		try:
			user_obj = User.objects.get(id=user_id)
		except Exception as e:
			# raise e
			return Response( {"error":"User not exist."} , status=403)

		user = {
			"first_name": 	request.data.get('first_name', "" ),
			"last_name": 	request.data.get('last_name', "" ),

			"mobile_no": 	request.data.get("mobile_no", None ),
			"gender": 		request.data.get("gender", None ),
		}
		serialized_profile = UserProfileSerializer(user_obj, data = user)
		
		if serialized_profile.is_valid()  :
			res_user_profile = serialized_profile.update(instance=user_id, validated_data=user)
			# return Response(  status=204 )
			return Response( res_user_profile , status=200 )
		else:
			if serialized_profile.errors:
				return Response( serialized_profile.errors , status=400)
 
		return Response({"details": "Invaild request data."}, status=400)


	# def patch(self, request, format=None):
	# 	user = UserSerializer(data=request.data)
	# 	if user.is_valid():
	# 		user.update(instance=request.user)
	# 		return Response(HTTP_200_OK)

class LogoutUser(APIView):
	def get(self, request, format=None):
		"""simply delete the token to force a login"""
		request.user.auth_token.delete()
		return Response(status=status.HTTP_200_OK)

# @api_view(['POST',])
# def register_user(request):
	# print("test=", request.data)
	# request.data.push('is_staff', 'True')
	# print("test=", request.data)

	# serialized = UserSerializer(data = request.data)
	
	# if serialized.is_valid() :
	# 	user = User.objects.create_user(serialized.save())
	# 	return Response( serialized.data , status=status.HTTP_201_CREATED)
	# else:
	# 	return Response(serialized.errors, status=400)

	# queryset = UserProfileSerializer.create(request.data)

	# print("test=", user)
	# return Response( user , status=status.HTTP_201_CREATED)

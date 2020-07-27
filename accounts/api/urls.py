from django.urls import path, include
from . import views


from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
	
	# path('register/', views.index ),
	# path('test/', views.test ),
	path('register/', views.UserCreate.as_view(), name='register_user'),
	path('update/<int:user_id>/', views.UserProfileUpdate.as_view(), name='update_user_profile'),
	path('logout/', views.LogoutUser.as_view(), name='LogoutUser'),
	# path('register/', views.register_user, name='register_user'),
	# path('', views.UserView.as_view() ),
	
	# path('test2/', views.Home.as_view()),


	path('', views.HelloView.as_view(), name='HelloView'),
	path('upload_profile/<int:user_id>/', views.UploadProfilePicture.as_view(), name='UploadProfilePicture'),


	# NEW: custom verify-token view which is not included in django-rest-passwordreset
	# path('reset-password/verify-token/', acc_views.CustomPasswordTokenVerificationView.as_view(), name='password_reset_verify_token'),
 #    # NEW: The django-rest-passwordreset urls to request a token and confirm pw-reset
 #    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),


 	# Router url
 	path('', include(router.urls)),

]



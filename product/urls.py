from . import views

from django.contrib import admin
from django.urls import path
from django.conf.urls import url

urlpatterns = [
	path('<str:product_slug>/', views.index, name='product'),
	path('<str:category_slug>/<str:product_slug>/', views.index, name='product'),
	 

]
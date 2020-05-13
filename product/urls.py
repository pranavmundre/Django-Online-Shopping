from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from . import views 

urlpatterns = [
	path('<str:product_slug>/', views.index, name='product_page'),
	path('<str:category_slug>/<str:product_slug>/', views.index, name='product'),
	 

]


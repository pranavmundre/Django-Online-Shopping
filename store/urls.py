from . import views


from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('signin/', views.sign_in, name='sign_in'),
    path('signin/', views.sign_out, name='sign_out'),
    path('register/', views.register, name='register'),
]
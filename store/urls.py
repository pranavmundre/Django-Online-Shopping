from . import views

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
	path('', views.index, name='home'),
	path('signin/', views.sign_in, name='sign_in'),
	path('signin/', views.sign_out, name='sign_out'),
	path('register/', views.register, name='register'),


	path('contact/',TemplateView.as_view(template_name='contact-us.html')),

	url(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type = 'text/plain')),
	# url(r'^sitemap.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type = 'application/xml')),
	url(r'^sitemap.xml$', views.sitemap, name='sitemap'),
]
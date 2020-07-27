"""OnlineShopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.urls import include, path
	2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import handler404, handler500, url
from store import views as store_views, pwa_views  

from rest_framework.authtoken.views import obtain_auth_token
from accounts import views
from django.views.static import serve


admin.site.site_header = 'Shopping Administration'                    # default: "Django Administration"
# admin.site.index_title = 'Hotel Administration'                 # default: "Site administration"
# admin.site.site_title = 'Admin Of Online Hotel Management' # default: "Django site admin"





urlpatterns = [
	path('', include('store.urls')),
	path('product/', include('product.urls')),
	path('superadmin/', admin.site.urls),
	path('account/', include("accounts.urls")),

	# path('pwa/', include('pwa.urls')),
	url(r'^serviceworker.js$', pwa_views.service_worker),
    url(r'^manifest.json$', pwa_views.manifest),

	# API URLS
	path('api/product/', include('product.api_urls')),





    # REST API FRAMEWORK 
    path('api/account/', include('accounts.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

] 
# + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

handler404 = store_views.error_400
#  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
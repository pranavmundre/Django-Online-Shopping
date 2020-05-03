from django.urls import path
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from . import  api

api_urlpatterns = [
	path('', api.get_product_list ),
	path('<int:product_id>/', api.get_single_product ),
]

urlpatterns = format_suffix_patterns(api_urlpatterns)


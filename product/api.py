
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from .models import Product
from .serializers import ProductSerializer, CategorySerializer
# from .serializers import ProductSerializer, CategorySerializer, PriceSerializer, ShippingSerializer

# Create your API here.


@api_view([ 'GET', 'POST'])
def get_product_list(request ):
	context = {'message':''}
	try:
		products = Product.objects.all()
		serializer = ProductSerializer( products, many=True )
		print("testz=ok")
	except Exception as e:
		return Response(status=status.HTTP_400_BAD_REQUEST)
		# raise e
	return Response(serializer.data )


@api_view([ 'GET', 'POST'])
def get_single_product(request, product_id ):
	context = {'message':''}
	try:
		product = Product.objects.get(id=product_id)
		serializer = ProductSerializer( product  )
	except Exception as e:
		# raise e
		context.update(message='Product not found')
		return Response(data=context ,status=status.HTTP_400_BAD_REQUEST)

	return Response(serializer.data )

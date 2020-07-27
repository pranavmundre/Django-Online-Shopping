from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index( request):
	# return HttpResponse("Hello World@")
	# print(request.META['HTTP_HOST']

	return render( request, "index.html" )

def test( request):
	return HttpResponse("Hello World@")



def live_web_msg( request):
	return render( request, "live-web.html" )
	
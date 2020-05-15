
from OnlineShopping.settings import MEDIA_URL, MEDIA_ROOT
from django.http import HttpResponse
import os, time, datetime

from uuid import uuid4
# rand_token = uuid4().hex[:6]


def create_qr_code(request):
	import pyqrcode 
	html_data= ''

	today = datetime.date.today()  
	data = "Welcome to QR code"
	qr_formate = '.svg'
	file_name = 'qr_code'

	qr_image = pyqrcode.create(data) #Create QR Code
	dir_path = 'product_qr_code/'+today.strftime("%Y/%m/%d/")

	while True:
		rand_token = uuid4().hex[:6]
		file = file_name+'_'+rand_token+qr_formate
		if not os.path.exists(dir_path+file):
			break

	try:
		path = os.path.join(MEDIA_ROOT, dir_path )
		os.makedirs(path)
	except Exception as e:
		# print("Error:", e)
		# raise e
		pass

	file_path = dir_path+file
	# qr_image.svg(MEDIA_ROOT+file_path) #Save QR Code

	html_data += '<img src="'+MEDIA_URL+file_path+'" width="300">'
	return HttpResponse(html_data)


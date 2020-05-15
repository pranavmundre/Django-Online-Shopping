from django.shortcuts import render
from django.http import HttpResponse
from OnlineShopping import pwa_settings

def service_worker(request):
	response = HttpResponse(open(pwa_settings.PWA_SERVICE_WORKER_PATH).read(), content_type='application/javascript')
	return response


def manifest(request):
	return render(request, 'manifest.json', {
		setting_name: getattr(pwa_settings, setting_name)
		for setting_name in dir(pwa_settings)
		if setting_name.startswith('PWA_')
	})
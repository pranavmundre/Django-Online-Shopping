from django.conf import settings


def site_info(request):
	return {
		'APPLICATION_NAME': settings.APPLICATION_NAME, 
		'SITE_URL': settings.SITE_URL,
		'FULL_MEDIA_URL': settings.FULL_MEDIA_URL,
	}

 
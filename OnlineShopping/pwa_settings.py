import os
from OnlineShopping.settings import BASE_DIR

# PWA Setting 

# PWA_APP_DEBUG_MODE = False
PWA_APP_NAME = 'Online Shopping' 
PWA_APP_DESCRIPTION = "Online shop" 
PWA_APP_THEME_COLOR = '#0A0302' 
PWA_APP_BACKGROUND_COLOR = '#fff' 
PWA_APP_DISPLAY = 'standalone' 
PWA_APP_SCOPE = '/' 
PWA_APP_ORIENTATION = 'any' 
PWA_APP_START_URL = '/' 
PWA_APP_ICONS = [ { 'src': '/static/images/logo/150x150.png', 'sizes': '150x150' } ] 
PWA_APP_ICONS_APPLE = [ { 'src': '/static/images/logo/150x150.png', 'sizes': '150x150' } ] 
PWA_APP_SPLASH_SCREEN = [ { 
	'src': '/static/images/logo/150x150.png', 
	'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)' 
} ] 
PWA_APP_DIR = 'ltr' 
PWA_APP_LANG = 'en-US'
PWA_SERVICE_WORKER_PATH =  os.path.join(BASE_DIR, 'template/pwa/serviceworker.js')
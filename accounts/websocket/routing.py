from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import LiveScoreConsumer


# websockets = URLRouter([
#     path("ws/get-data/", LiveScoreConsumer,    name="live-web", ),
# ])


websocket_urlpatterns =  [
    path("r^ws/get-data/", LiveScoreConsumer,  name="live-web", ),
]
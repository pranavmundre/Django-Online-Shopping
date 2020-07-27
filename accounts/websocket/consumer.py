# Built in imports.
import json
# Third Party imports.
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
# Django imports.
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
# Local imports.
# from my_proj.game.models import Game
# from my_proj.game.utils import get_live_score_for_game


class LiveScoreConsumer(AsyncWebsocketConsumer):
	async def connect(self):
	   # self.room_name = self.scope['url_route']['kwargs']['game_id']
	   # self.room_group_name = f'Game_{self.room_name}'
	   # if self.scope['user'] == AnonymousUser():
	   #     raise DenyConnection("Invalid User")
	   # await self.channel_layer.group_add(
	   #     'self.room_group_name',
	   #     self.channel_name
	   # )
	   # # If invalid game id then deny the connection.
	   # try:
	   #      self.game = Game.objects.get(pk=self.room_name)
	   # except ObjectDoesNotExist:
	   #      raise DenyConnection("Invalid Game Id")
	   # await self.accept()
	   await self.connect()

	async def receive(self, text_data):
	   # game_city = json.loads(text_data).get('game_city')
	 #   await self.channel_layer.group_send(
		# 	'self.room_group_name',
		# 	{
		# 		'type': 'live_score',
		# 		'game_id': 'self.room_name',
		# 		'game_city': 'game_city'
		# 	}

		# )
		# text_data_json = json.loads(text_data)
		# message = text_data_json['message']

		# self.send(text_data=json.dumps({
		# 	'message': 'message'
		# }))
		print(">>>>>>", text_data)
		pass


	def disconnect(self, close_code):
		await self.disconnect()
		
	# async def live_score(self, event):
	# 	# city = event['game_city']
	# 	# Here helper function fetches live score from DB.
	# 	await self.send(text_data=json.dumps({
	# 			'score': 'get_live_score_for_game(self.game, city)'
	# 		}))


	# async def websocket_disconnect(self, message):
	# 	# Leave room group
	# 	await self.channel_layer.group_discard(
	# 		'self.room_group_name',
	# 		self.channel_name
	# 	)

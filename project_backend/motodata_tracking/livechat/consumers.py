import json
from channels.generic.websocket import WebsocketConsumer
from .models import ChatMessage

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = self.scope['user'].username

        self.save_message(username, self.room_name, message)
        self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
        }))
   
    def save_message(self, username, room, message):
        ChatMessage.objects.create(sender=username, room=room, content=message)
from django.db import models

class ChatMessage(models.Model):
    user_message = models.TextField()
    chatbot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

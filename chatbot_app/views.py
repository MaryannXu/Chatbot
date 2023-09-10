from django.shortcuts import render
from django.http import JsonResponse
import openai

from chatbot_app.models import ChatMessage
from chatbot_project import settings

def chatbot(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        chatbot_response = generate_chatbot_response(user_message)
        save_chat_message(user_message, chatbot_response)
        return JsonResponse({'response': chatbot_response})
    return render(request, 'chatbot_app/chatbot.html')

def generate_chatbot_response(user_message):
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the GPT-3.5-turbo model
        messages=[
            {"role": "system", "content": "You are a helpful chatbot"},
            {"role": "user", "content": user_message},
        ],
        max_tokens=1000,
        temperature=0.7,
    )
    return response.choices[0].message["content"]

def save_chat_message(user_message, chatbot_response):
    ChatMessage.objects.create(
        user_message=user_message,
        chatbot_response=chatbot_response
    )
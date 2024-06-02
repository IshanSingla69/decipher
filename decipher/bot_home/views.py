from django.shortcuts import render
from django.http import JsonResponse
from . import bot_decipher as bot

# Create your views here.
def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("user-input")
        print(user_input)
        response = bot.UserQuery(user_input)
        print(response.text)
        return render(request, "bot_home/chatbot.html")

    return render(request, "bot_home/chatbot.html")
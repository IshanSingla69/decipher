from django.shortcuts import render,redirect
from django.http import HttpResponse
from .decipher_bot import decipher
from django.http import HttpResponse

notion_page_id = "3411ec690b544b14bf57b99eb052f3e4"
integeration_token = "secret_ni7kJlPLPcaPmVlZCgXG2QDmz0xR7p1SL9Mg2MWTh52"

def chatbot_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('user-prompt')
        print(prompt)
        if prompt:
            decipher.CreateNotionPage(notion_page_id, integeration_token, prompt)
            context ={
                'prompt':prompt,
                'success': True
            }
            return render(request, "bot_home/chatbot.html", context)
    return render(request, "bot_home/chatbot.html")

def success_view(request):
    return redirect("chatbot_view")
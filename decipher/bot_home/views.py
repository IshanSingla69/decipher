from django.shortcuts import render,redirect
from django.http import HttpResponse



def chatbot_view(request):
    if request.method == 'POST':
        prompt_text = request.POST.get('prompt', '')
        print(prompt_text) 
        return render(request,"bot_home/chatbot.html",{"prompt":prompt_text})
    else:
        return render(request,"bot_home/chatbot.html")

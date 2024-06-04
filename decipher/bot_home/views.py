from django.shortcuts import render,redirect
from django.http import HttpResponse
from .decipher_bot import decipher
# Create your views here.
def chatbot_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('user-prompt')
        print(prompt)
        if prompt:
            decipher.SetUserPrompt(prompt)
            keywords = decipher.GetKeywords()
            decipher.GetIntroduction(keywords)
            decipher.WriteAndFilterLinks(keywords)
            decipher.GetYoutubeLinks(keywords)
            context ={
                'prompt':prompt,
                'keywords':keywords,
                'success': bool(keywords)
            }
            return render(request, "bot_home/chatbot.html", context)
    return render(request, "bot_home/chatbot.html")

def success_view(request):
    return redirect("chatbot_view")
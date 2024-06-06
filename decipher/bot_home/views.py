from django.shortcuts import render,redirect
from django.http import HttpResponse
from .decipher_bot import decipher
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# from .decipher_bot.telegram_bot.events import Publisher, Subscriber

notion_page_id = "3411ec690b544b14bf57b99eb052f3e4"
integeration_token = "secret_ni7kJlPLPcaPmVlZCgXG2QDmz0xR7p1SL9Mg2MWTh52"

notion_page_id:str = ""
integeration_token:str = ""
details_confirmed:bool = False



# def set_user_details(_integeration_token, _notion_page_id):
#     global notion_page_id
#     global integeration_token
#     global details_confirmed
#     notion_page_id = _notion_page_id
#     integeration_token = _integeration_token
#     details_confirmed = True
#     redirect("chatbot_view")

# set_user_details_subscriber = Subscriber('details_confirmed', set_user_details)
# Publisher.register('details_confirmed', set_user_details_subscriber)

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
    # if details_confirmed:
    #     if request.method == 'POST':
    #         prompt = request.POST.get('user-prompt')
    #         print(prompt)
    #         if prompt:
    #             decipher.CreateNotionPage(notion_page_id, integeration_token, prompt)
    #             context ={
    #                 'prompt':prompt,
    #                 'success': True
    #             }
    #             return render(request, "bot_home/chatbot.html", context)
    #     return render(request, "bot_home/chatbot.html")
    # else:
    #     return HttpResponse("Please set your integration token and page id first " + details_confirmed.__str__() + " page id: "+ notion_page_id + " integration token " + integeration_token)
    

def dashboard_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('user-prompt')
        print(prompt)
        if prompt:
            decipher.CreateNotionPage(notion_page_id, integeration_token, prompt)
            context ={
                'prompt':prompt,
                'success': True
            }
            return render(request, "bot_home/dashboard.html", context)
        return redirect("chatbot_view")
    return render(request, "bot_home/dashboard.html")


def success_view(request):
    return redirect("chatbot_view")
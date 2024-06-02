from django.shortcuts import render,redirect
# Create your views here.
def chatbot_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        print(prompt)
        if prompt:
            return redirect("bot_home/success.html")
    return render(request, "bot_home/chatbot.html")
from . import googlesrch as gsearch
from . import youtubesrch as ytsearch
from . import ConfigureSettings as _conf
import os

if not os.path.exists('bot_home/decipher_bot/result_files'):
    os.makedirs('bot_home/decipher_bot/result_files')

PATH = 'bot_home/decipher_bot/result_files/'

model = _conf.configureGemini()
def SetUserPrompt(prompt):
    global userprompt
    userprompt = prompt

def GetKeywords():
    query = "Identify key topic word. Less than 5 words. Only from the prompt. User's prompt is: " + userprompt
    
    keywords = queryGemini(query)
    
    gsearch.searchQuery(keywords)
    print(keywords)
    return keywords

def WriteAndFilterLinks(topic):
    gsearch.filter_links(topic)

def GetYoutubeLinks(topic):
    ytsearch.searchQuery(topic, 5)
    return True

def GetIntroduction(topic):
    query = "Tell me about "+topic+" in brief. Include its origin, applications, and other relevant information."

    introduction = queryGemini(query)
    file = open(PATH+"intro.txt", 'w')
    file.write(introduction)
    file.close
    return introduction

def queryGemini(query):
    chat_session = model.start_chat(history=[])

    #Find keywords
    response = chat_session.send_message(query)
    return response.text
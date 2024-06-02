import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

def UserQuery(prompt):
    query = "user is a learner, user needs to spend 30 mins on this topic, user is a beginner, provide the learning resources from the internet, first tell the brief introduction about the topic, then provide links to the official or famous websites/articles around the topic, provide a youtube link to learn more about the topic, give links to famous courses on udemy and coursera on that particular topic. the user's prompt is" + prompt
    response = chat_session.send_message(query)
    return response

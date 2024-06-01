from django.urls import path
from . import views
path('', views.chatbot_view, name="chatbot_view"),
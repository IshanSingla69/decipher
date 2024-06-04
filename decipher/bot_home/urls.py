from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name="chatbot_view"),
    path('success/', views.success_view, name="success_view"),
]

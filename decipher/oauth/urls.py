from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login,name='login'),
    path('logout/', views.logout_view, name='logout'),
]

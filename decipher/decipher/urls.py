from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),

    path('dashboard/', include('bot_home.urls'),name="dashboard"),
    path('', include('oauth.urls')),
]

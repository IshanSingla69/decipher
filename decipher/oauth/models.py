from django.db import models
from django.contrib.auth.models import User


class ApiKeys(models.Model):
    user_mail = models.OneToOneField(User, on_delete=models.CASCADE)
    key_id = models.CharField(max_length=255)
    key_page = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.user.username}"


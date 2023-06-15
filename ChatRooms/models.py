from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room (models.Model):
    name = models.CharField(max_length=30)
    disponibility = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Message (models.Model):
    message = models.CharField(max_length=370)
    datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

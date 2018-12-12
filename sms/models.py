# Create your models here.
from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=200)
    desp = models.TextField()
    msg_date = models.DateTimeField('sms message sent time', auto_now_add=True)

from django.db import models
from profiles.models import User


class Information(models.Model):
    name = models.CharField(max_length=128)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=128)
    content = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"From {self.user} concerning {self.subject} : {self.date_added.strftime('%d.%m.%Y %H:%M')}")



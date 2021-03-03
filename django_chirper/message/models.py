from django.db import models
from user.models import Profile
from django.utils import timezone


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'sent')
    recipient = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'received')
    body = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)

    def __repr__(self):
        return f'{self.sender} sent "{self.body}" to {self.recipient}.'
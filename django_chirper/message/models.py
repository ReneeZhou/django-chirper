from django.db import models
from django.utils import timezone
from user.models import Profile


class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'sent')
    recipient = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'received')
    body = models.TextField()
    created_at = models.DateTimeField(default = timezone.now)
    liker = models.ManyToManyField(Profile, related_name = 'liked_messages')

    def __repr__(self):
        return f'''
        {self.sender.user.username.title()} | {self.recipient.user.username.title()}: 
        {self.body}
        '''

    def __str__(self):
        return f'''
        {self.sender.user.username.title()} | {self.recipient.user.username.title()}: 
        {self.body}
        '''
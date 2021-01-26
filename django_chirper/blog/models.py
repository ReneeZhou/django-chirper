from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.CharField(max_length = 280)
    created_at = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    # if the author is deleted, so will all its posts; one-way only

    def __repr__(self):
        return f'{self.content} by {self.author};'
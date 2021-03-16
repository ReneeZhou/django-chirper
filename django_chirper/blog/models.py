from secrets import randbits
from datetime import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse
from user.models import Profile


def gen_key(bits = 60):
    return randbits(bits)


class Post(models.Model):
    id = models.BigAutoField(primary_key = True, default = gen_key)
    content = models.CharField(max_length = 280)
    created_at = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(Profile, on_delete = models.CASCADE)
    # if the author is deleted, so will all its posts; one-way only
    liker = models.ManyToManyField(Profile, related_name = 'liked_posts')

    @property
    def show_time(self):
        naive = self.created_at.replace(tzinfo = None)
        t = datetime.utcnow() - naive
        if t.seconds < 59:
            return f'{t.seconds}s'
        elif 50 <= t.seconds < 3600:
            return f'{t.seconds//60}m'
        elif t.days < 1:
            return f'{t.seconds//3600}h'
        elif self.created_at.year == datetime.utcnow().year:
            return self.created_at.strftime('%d %b')
        else: 
            return self.created_at.strftime('%d %b %Y')

    def __repr__(self):
        return f'{self.author.user.username.title()} | {self.content}'

    def __str__(self):
        return f'{self.author.user.username.title()} | {self.content}'

    def get_absolute_url(self):
        return reverse('status', kwargs = {'handle': self.author.handle, 'pk': self.id})
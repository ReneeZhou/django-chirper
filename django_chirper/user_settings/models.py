from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_image = models.ImageField(default = 'default_profile.png', upload_to = 'profile_pics')
    background_image = models.ImageField(default = 'default_background.png', upload_to = 'background_pics')
    bio = models.TextField(max_length = 160, blank = True)
    location = models.TextField(max_length = 30, blank = True)
    website = models.URLField(max_length = 100, blank = True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def __repr__(self):
        return f'{self.user.username}\'s Profile' 
from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_image = models.ImageField(default = 'default_profile.png', upload_to = 'profile_pics')
    background_image = models.ImageField(default = 'default_background.png', upload_to = 'background_pics')
    bio = models.TextField(max_length = 160, blank = True)
    location = models.TextField(max_length = 30, blank = True)
    website = models.URLField(max_length = 100, blank = True)

    # override save() in the Model class
    def save(self):
        super().save()                                                      # first run the parent's save method
        output_size = {'profile': (400, 400), 'background': (600, 200)}
        p_img = Image.open(self.profile_image.path)
        b_img = Image.open(self.background_image.path)

        if p_img.width > 400 or p_img.height > 400:
            p_img.thumbnail(output_size.get('profile'))
            p_img.save(self.profile_image.path)

        if b_img.width > 600 or p_img.height > 200:
            b_img.thumbnail(output_size.get('background'))
            b_img.save(self.background_image.path)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def __repr__(self):
        return f'{self.user.username}\'s Profile' 
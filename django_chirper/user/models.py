from secrets import randbits, token_urlsafe
from PIL import Image
from django.db import models
from django.db.models.query_utils import Q
from django.contrib.auth.models import User


def gen_key(bits = 60):
    return randbits(bits)
    
def gen_hex(bytes = 5):
    return token_urlsafe(bytes)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    id = models.AutoField(primary_key = True, default = gen_key)
    created_at_ip = models.GenericIPAddressField(null = True, blank = True)
    handle = models.TextField(default = gen_hex, unique = True)
    phone = models.CharField(max_length = 20, null = True, blank = True, unique = True)
    birthdate = models.DateField(null = True, blank = True)

    profile_image = models.ImageField(default = 'default_profile.png', upload_to = 'profile_pics')
    background_image = models.ImageField(default = 'default_background.png', upload_to = 'background_pics')
    bio = models.TextField(max_length = 160, blank = True)
    location = models.TextField(max_length = 30, blank = True)
    website = models.URLField(max_length = 100, blank = True)

    following = models.ManyToManyField(
        'self', 
        symmetrical = False,
        through = 'Follower',
        # through_fields = ('profile', 'profile')     # not needed to itself w/ 2 ForeignKey
    )

    # override save() in the Model class
    def save(self, *args, **kwargs):
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


class Follower(models.Model):
    follower = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'is_following')
    following = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'followed_by')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['follower', 'following'], name = 'unique_relationship'),
        ]

    def __repr__(self):
        return f'{self.follower} is following {self.following}.'
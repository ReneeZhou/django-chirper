from secrets import randbits, token_urlsafe
from PIL import Image
import pycountry
from phonenumbers import COUNTRY_CODE_TO_REGION_CODE
from django.db import models
from django.db.models.expressions import Q
from django.db.models.fields import DateTimeField
from django.contrib.auth.models import User
from django.utils import timezone


def gen_key(bits = 60):
    return randbits(bits)
    
def gen_hex(bytes = 5):
    return token_urlsafe(bytes)


class Profile(models.Model):
    choices = []
    for code, countries in COUNTRY_CODE_TO_REGION_CODE.items():
        for country in countries: 
            try:
                choices.append([
                    '+' + str(code),
                    '+' + str(code) + ' ' + pycountry.countries.get(alpha_2 = country).name
                ])
            except AttributeError:
                pass
    choices = [[None, '']] + [[i, j.split(',')[0]] for i, j in choices]
                

    user = models.OneToOneField(User, on_delete = models.CASCADE)

    id = models.BigAutoField(primary_key = True, default = gen_key)
    created_at_ip = models.GenericIPAddressField(null = True, blank = True)
    handle = models.TextField(
        default = gen_hex,
        unique = True, 
        error_messages={
            'unique': 'That username has been taken. Please choose another.'
        }
    )
    country_code = models.CharField(max_length = 200, null = True, choices = choices)
    phone = models.CharField(max_length = 20, null = True, blank = True, unique = True)
    phone_public = models.BooleanField(default = True)
    birthdate = models.DateField(null = True, blank = True)

    profile_image = models.ImageField(default = 'default_profile.png', upload_to = 'profile_pics')
    background_image = models.ImageField(default = 'default_background.png', upload_to = 'background_pics')
    bio = models.TextField(max_length = 160, null = True, blank = True)
    location = models.TextField(max_length = 30, null = True, blank = True)
    website = models.URLField(max_length = 100, null = True, blank = True)

    following = models.ManyToManyField(
        'self', 
        symmetrical = False,
        through = 'Following',
        # through_fields = ('profile', 'profile')     # not needed to itself w/ 2 ForeignKey
    )

    last_checked_message_at = DateTimeField(default = timezone.now)

    @property
    def new_message(self):
        if len(self.received.all()) == 0:
            return False
        elif self.received.order_by('-created_at').first().created_at > self.last_checked_message_at:
            return True

    @property
    def follow_recommendation(self):
        recommendation = Profile.objects.exclude(
            Q(handle__in = self.following.values('handle')) |
            Q(handle = self.handle)
        ).order_by('?')[:3]
        return recommendation


    # disable to avoid PIL conflict with s3
    # will do it through s3 lambda
    # override save() in the Model class
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)                                                      # first run the parent's save method
    #     output_size = {'profile': (400, 400), 'background': (600, 200)}
    #     p_img = Image.open(self.profile_image.path)
    #     b_img = Image.open(self.background_image.path)

    #     if p_img.width > 400 or p_img.height > 400:
    #         p_img.thumbnail(output_size.get('profile'))
    #         p_img.save(self.profile_image.path)

    #     if b_img.width > 600 or p_img.height > 200:
    #         b_img.thumbnail(output_size.get('background'))
    #         b_img.save(self.background_image.path)

    def __repr__(self):
        return f'{self.user.username.title()}'

    def __str__(self):
        return f'{self.user.username.title()}'


class Following(models.Model):
    follower = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'is_following')
    following = models.ForeignKey(Profile, on_delete = models.CASCADE, related_name = 'followed_by')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['follower', 'following'], name = 'unique_relationship'),
        ]

    def __repr__(self):
        return f'''
        {self.follower.user.username.title()} 
        | 
        {self.following.user.username.title()}
        '''

    def __str__(self):
        return f'''
        {self.follower.user.username.title()} 
        | 
        {self.following.user.username.title()}
        '''
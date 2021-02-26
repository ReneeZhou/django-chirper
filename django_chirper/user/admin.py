from django.contrib import admin
from .models import Profile, Follower

class FollowerInline(admin.TabularInline):
    model = Follower
    fk_name = 'following'

class ProfileAdmin(admin.ModelAdmin):
    inlines = [FollowerInline]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Follower)
from django.contrib import admin
from .models import Profile, Following

class FollowingInline(admin.TabularInline):
    model = Following
    fk_name = 'following'

class ProfileAdmin(admin.ModelAdmin):
    inlines = [FollowingInline]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Following)
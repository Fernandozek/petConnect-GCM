from django.contrib import admin

from ..models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1
    can_delete = False
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .profile_inline import ProfileInline


# Define the custom admin user
class UserCustomAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Register the custom admin user
admin.site.unregister(User)
admin.site.register(User, UserCustomAdmin)

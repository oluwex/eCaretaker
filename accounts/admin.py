from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import RealUsers

class RealUserInline(admin.StackedInline):
    model = RealUsers
    can_delete = False
    # verbose_name = 'Additional user information'
    verbose_name_plural = 'Additional user information'

class UserAdmin(BaseUserAdmin):
    inlines = (RealUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
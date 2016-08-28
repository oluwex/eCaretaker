from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# from .models import RealUsers
#
# # Register your models here.
#
# from .models import Users
#
# class UserModelAdmin(admin.ModelAdmin):
#     list_display_links = ['username']
#     list_display = ['username', 'email', 'last_name', 'first_name', 'middle_name', 'joined', 'updated']
#     list_filter = ['role']
#     search_fields = ['role', 'username']
#
#     class Meta:
#         model = Users
#
# class RealUserInline(admin.StackedInline):
#     model = RealUsers
#     can_delete = False
#     verbose_name_plural = 'users'
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (RealUserInline,)
#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(Users, UserModelAdmin)
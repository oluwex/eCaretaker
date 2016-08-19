from django.contrib import admin

# Register your models here.

from .models import Users

class UserModelAdmin(admin.ModelAdmin):
    list_display_links = ['username']
    list_display = ['username', 'email', 'last_name', 'first_name', 'middle_name', 'joined', 'updated']
    list_filter = ['role']
    search_fields = ['role', 'username']

    class Meta:
        model = Users

admin.site.register(Users, UserModelAdmin)
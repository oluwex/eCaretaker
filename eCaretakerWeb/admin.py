from django.contrib import admin

# Register your models here.

from .models import State, LGA

class StateModelAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['name']
    list_editable = ['name']

    class meta:
        model = State

class LGAModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'stateId']
    list_display_links = ['name']
    list_filter = ['stateId']
    search_fields = ['name', 'stateId']

    class meta:
        model = LGA

admin.site.register(State, StateModelAdmin)
admin.site.register(LGA, LGAModelAdmin)
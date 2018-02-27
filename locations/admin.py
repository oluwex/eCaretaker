from django.contrib import admin
from .models import LGA, State, City, Street, House

# Register your models here.


class HouseModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'house_no', 'street', 'city', 'local_government', 'state', 'owner']
    list_display_links = ['name']
    list_filter = ['city', 'state',]
    search_fields = ['name', 'street']

    class Meta:
        model = House

class StreetModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'local_government', 'state']
    list_display_links = ['name']
    list_filter = ['city', 'state']
    search_fields = ['name', 'city']

    class Meta:
        model = Street

class CityModelAdmin(admin.ModelAdmin):
    list_display = ['name','local_government', 'state']
    list_display_links = ['name']
    list_filter = ['local_government', 'state']
    search_fields = ['name', 'state']

    class Meta:
        model = City

class LGAModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'stateId']
    list_display_links = ['name']
    list_filter = ['stateId']
    search_fields = ['name', 'stateId']

    class meta:
        model = LGA

class StateModelAdmin(admin.ModelAdmin):
    list_display_links = None
    list_display = ['name']
    list_editable = ['name']

    class meta:
        model = State


admin.site.register(House, HouseModelAdmin)
admin.site.register(Street, StreetModelAdmin)
admin.site.register(City, CityModelAdmin)
admin.site.register(LGA, LGAModelAdmin)
admin.site.register(State, StateModelAdmin)

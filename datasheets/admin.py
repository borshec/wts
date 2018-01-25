from django.contrib import admin
from .models import Datasheet, Package, Manufacturer


class DatasheetAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'description', )
    actions_on_top = True
    actions_on_bottom = True
    date_hierarchy = 'creation_date'


admin.site.register(Datasheet, DatasheetAdmin)
admin.site.register((Package, Manufacturer))

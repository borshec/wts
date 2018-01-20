from django.contrib import admin
from .models import Datasheet, Package, Manufacturer

admin.site.register((Datasheet, Package, Manufacturer))
# Register your models here.

from django.contrib import admin
from django.forms import forms, ModelForm
from django.forms.widgets import FileInput, TextInput, ClearableFileInput, SelectDateWidget
from django.forms.widgets import DateTimeInput
from .models import Datasheet, Package, Manufacturer

class DatasheetAdminForm(ModelForm):
    class Meta:
        model = Datasheet
        fields = '__all__'
        widgets = {'dsfile': DateTimeInput(),}

class DatasheetAdmin(admin.ModelAdmin):
    form = DatasheetAdminForm

admin.site.register(Datasheet, DatasheetAdmin)

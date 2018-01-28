from django.contrib import admin
from django.forms import forms, ModelForm
from django.forms.widgets import FileInput, TextInput, ClearableFileInput, SelectDateWidget
from django.forms.widgets import DateTimeInput
from .models import Datasheet, Package, Manufacturer

class DatasheetAdminForm(ModelForm):
    class Meta:
        model = Datasheet

        fields = '__all__'
        widgets = {'dsfile': ClearableFileInput(),}
# value parameter for ClearableFileInput.render  - a django file object with url attribute

class DatasheetAdmin(admin.ModelAdmin):
    form = DatasheetAdminForm
    list_display = ('id', 'dsfile', 'description', 'initial_filename')

admin.site.register(Datasheet, DatasheetAdmin)

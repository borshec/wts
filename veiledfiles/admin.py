from django.contrib import admin
from veiledfiles.models import VeiledFile, TestModel

admin.site.register((VeiledFile, TestModel))
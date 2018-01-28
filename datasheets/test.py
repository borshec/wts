import django
django.setup()
from datasheets.models import Datasheet
from django.forms.widgets import ClearableFileInput

ds = Datasheet.objects.get(id=9)
cfi = ClearableFileInput()

print("")
print(cfi.render("cfi", ds.dsfile))
print("")
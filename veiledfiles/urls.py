from django.urls import path
from veiledfiles import views

urlpatterns = [
    path('<filename>', views.get_file)
]
from django.shortcuts import render, get_object_or_404
from veiledfiles.models import VeiledFile
from django.http import HttpResponse
import pdb

# Create your views here.

def get_file(request, filename):
    obj = get_object_or_404(VeiledFile, file = filename)
    response = HttpResponse(obj.file.read())
    response['content-type'] = obj.mime_type
    response['Content-Disposition'] = 'attachment; filename={}'.format(obj.file.initial_filename)
    return response
    # TODO: implement file transmit by x-sendfile

from django.shortcuts import render, get_object_or_404
from veiledfiles.models import VeiledFile
from django.http import HttpResponse
from mimetypes import guess_type
import pdb

# Create your views here.

def get_file(request, filename):
    obj = get_object_or_404(VeiledFile, file = filename)
    filename = obj.file.initial_filename
    response = HttpResponse(obj.file.read())
    response['content-type'] = guess_type(filename)
    response['Content-Disposition'] = 'attachment; filename={}'.format(filename)
    return response
    # TODO: implement sile transile by x-sendfile

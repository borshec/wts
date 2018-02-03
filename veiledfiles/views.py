from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_real_url(request, filename):
    return HttpResponse("Ok!")

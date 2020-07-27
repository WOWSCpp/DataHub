from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from pathlib import Path

def home(request):
    return render(request, 'home.html')

def jump_to_upload_page(request):
    # if request.method == 'GET':
    print("jump_to_upload_page")
    return render(request, 'upload.html')
    # else:
    #     upload(request)
    #     return render(request, 'home.html')

def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")
 
    return HttpResponse("Failed")


def handle_uploaded_file(file, filename):
    path = '/home/ubuntu/'
    if not os.path.exists(path):
        os.mkdir(path)
 
    with open(path + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def download(request, path):
    pass
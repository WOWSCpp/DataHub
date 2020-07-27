from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from pathlib import Path

@csrf_exempt
def home(request):
    return render(request, 'list.html', {'what':'Django File Upload'})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")
 
    return HttpResponse("Failed")

 
def handle_uploaded_file(file, filename):
    path = '/home/Download/'
    if not os.path.exists(path):
        os.mkdir(path)
 
    with open(path + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
import os
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponse, Http404
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
    path = '/home/ubuntu/'
    if not os.path.exists(path):
        os.mkdir(path)
 
    with open(path + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

@csrf_exempt
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
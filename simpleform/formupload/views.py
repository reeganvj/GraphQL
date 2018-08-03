# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt

@csrf_exempt
def home(request):
    return render(request, 'index.html', {'what':'Django File Upload'})

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Uploaded Successfully !!!")
 
    return HttpResponse("Failed")

@csrf_exempt 
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
 
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


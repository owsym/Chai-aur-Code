from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Django home page")
    return render(request, 'webdite/index.html')

def about(request):
    return render(request, 'webdite/about.html')

def contact(request):
    return render(request, 'webdite/contact.html')
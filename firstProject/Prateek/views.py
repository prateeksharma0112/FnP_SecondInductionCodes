from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html', {})
    # return HttpResponse('Home Page')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("About US")

def resume(request):
    return render(request, 'resume.html')
    # return HttpResponse("Resume")
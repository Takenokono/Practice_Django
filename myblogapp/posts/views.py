from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello! : This page is for check of posts!")
# Create your views here.

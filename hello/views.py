from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    params = {
        'tittle':'Hello/Index',
        'msg' : 'これはテスト',
        'goto' : 'next',
    }
    return render(request,'hello/index.html',params)

def next(request):
    params = {
        'tittle':'Hello/next',
        'msg' : 'これはテスト',
        'goto' : 'index',
    }
    return render(request,'hello/index.html',params)
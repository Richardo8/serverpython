from django.shortcuts import render
from django.http import HttpResponse

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

def addOptimize(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c));


# Create your views here.

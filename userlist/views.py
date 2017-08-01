from django.shortcuts import render
from django.http import HttpResponse


def readFile(request):
    f = open('./userlist/Data/UserData.json', 'r')
    # print(f.read())
    data = f.read()
    print(data)
    return HttpResponse(data, content_type="application/json")


# Create your views here.

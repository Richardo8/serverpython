from django.shortcuts import render
from django.http import HttpResponse
from userlist.models import UserList
from django.core import serializers

def getAllUser(request):
    userlist = UserList.objects.all()
    returnData = serializers.serialize('json', userlist)
    return HttpResponse(returnData, content_type="application/json")


# Create your views here.

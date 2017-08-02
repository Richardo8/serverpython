from django.shortcuts import render
from django.http import HttpResponse
from userlist.models import UserList
from django.core import serializers
import json

def getAllUser(request):
    userlist = UserList.objects.all()
    returnData = serializers.serialize('json', userlist)
    # listData = list(userlist)
    # returnData = json.dumps(listData)
    # print(returnData)
    return HttpResponse(returnData, content_type="application/json")


# Create your views here.

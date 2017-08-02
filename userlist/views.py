from django.shortcuts import render
from django.http import HttpResponse
from userlist.models import UserList
from django.core import serializers

def readFile(request):
    # UserList.objects.create(uid=16, nick='asdf', name='sakgfsjdfg', sex='female', phone='13681111112', birthday='2013-1-1', address='cahgnan', latest='20140212', identity='chezhu')
    userlist = UserList.objects.all()
    returnData = serializers.serialize('json', userlist)
    f = open('./userlist/Data/UserData.json', 'r', encoding='utf8')
    print(userlist)
    data = f.read()
    # print(data)
    print(returnData)
    # return HttpResponse(returnData, content_type="application/json")
    return HttpResponse(returnData, content_type="application/json")


# Create your views here.

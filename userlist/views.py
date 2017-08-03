from django.shortcuts import render
from django.http import HttpResponse
from userlist.models import UserList
from django.core import serializers
import json

from django.forms.models import model_to_dict

def getAllUser(request):
    userlist = UserList.objects.all()
    returnList = []
    for e in userlist:
        print(e.uid)
        data = {
            "uid": e.uid,
            "nick": e.nick,
            "name": e.name,
            "sex": e.sex,
            "phone": e.phone,
            "birthday": e.birthday,
            "address": e.address,
            "latest": e.latest,
            "identity": e.identity
        }
        returnList.append(data)
    # 这种方式可以将数据提取出来，然后转化成json格式并传输
    returnList_json = json.dumps(returnList)
    # 可以使用以下方式对所获取的数据转化，但是转化之后的数据中有model和pk参数
    # returnData = serializers.serialize('json', userlist)
    return HttpResponse(returnList_json, content_type="application/json")


# Create your views here.

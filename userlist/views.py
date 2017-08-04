from django.shortcuts import render
from django.http import HttpResponse
from userlist.models import UserList
from django.core import serializers
from django.forms.models import model_to_dict
import json


from django.forms.models import model_to_dict

def getAllUser(request):
    userlist = UserList.objects.all()
    returnList = []
    for e in userlist:
        # strftime("%Y-%m-%d")可以将date类型数据转换成字符串类型
        data = {
            "uid": e.uid,
            "nick": e.nick,
            "name": e.name,
            "sex": e.sex,
            "phone": e.phone,
            "birthday": e.birthday.strftime("%Y-%m-%d"),
            "address": e.address,
            "latest": e.latest.strftime("%Y-%m-%d %H:%M:%S"),
            "identity": e.identity
        }
        returnList.append(data)
    # 这种方式可以将数据提取出来，然后转化成json格式并传输
    returnList_json = json.dumps(returnList)
    # 可以使用以下方式对所获取的数据转化，但是转化之后的数据中有model和pk参数
    # returnData = serializers.serialize('json', userlist)
    return HttpResponse(returnList_json, content_type="application/json")

def search(request):
    searchBody = json.loads(request.body)
    # # 该方法只能返回一条数据
    # searchResult = UserList.objects.get(name=searchBody['name'])
    # # 先将querySet实例转化成dict
    # searchResult_dict = [model_to_dict(searchResult)]
    # # 然后将dict转化成json，最后返回
    # searchResult_return = json.dumps(searchResult_dict)
    # print(searchResult_return)

    searchMore = UserList.objects.filter(name=searchBody['name'])
    returnList = []
    for e in searchMore:
        data = {
            "uid": e.uid,
            "nick": e.nick,
            "name": e.name,
            "sex": e.sex,
            "phone": e.phone,
            "birthday": e.birthday.strftime("%Y-%m-%d"),
            "address": e.address,
            "latest": e.latest.strftime("%Y-%m-%d %H:%M:%S"),
            "identity": e.identity
        }
        returnList.append(data)
    # 这种方式可以将数据提取出来，然后转化成json格式并传输
    returnList_json = json.dumps(returnList)

    return HttpResponse(returnList_json, content_type="application/json")

# Create your views here.

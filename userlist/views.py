from django.shortcuts import render
from django.http import HttpResponse
from userlist.models import UserList
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


def readFile(request):
    # UserList.objects.create(uid=16, nick='asdf', name='sakgfsjdfg', sex='female', phone='13681111112', birthday='2013-1-1', address='cahgnan', latest='20140212', identity='chezhu')
    # ulserlist = UserList.objects.all()
    f = open('./userlist/Data/UserData.json', 'r', encoding='utf8')
    # print(ulserlist)
    data = f.read()
    print(data)
    return HttpResponse(data, content_type="application/json")


# Create your views here.

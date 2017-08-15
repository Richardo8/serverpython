import os, json
from django.http import HttpResponse


def uploadPic(request):
    file_obj = request.FILES.get('avatar')
    print(file_obj)
    file_path = os.path.join('/Users/liushuo/Documents/Code/Study/React/reactirm/public/Pic', file_obj.name)
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    return HttpResponse(file_obj.name)

# Create your views here.

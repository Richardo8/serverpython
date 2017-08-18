import os, json
from django.http import HttpResponse


def uploadPic(request):
    file_obj = request.FILES.get('avatar')
    print(file_obj)
    # file_path = os.path.join('/Users/liushuo/Documents/Code/Study/React/reactirm/public/Pic', file_obj.name)
    file_path = os.path.join('common_static/images', file_obj.name)
    print(file_path)
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    return HttpResponse('static/images/' + file_obj.name, content_type="application/json")

# Create your views here.

import os, json
from django.http import HttpResponse


def uploadPic(request):
    file_obj = request.FILES.get('avatar')
    print(file_obj)
    file_path = os.path.join('article/static/images', file_obj.name)
    with open(file_path, 'wb') as f:
        for chunk in file_obj.chunks():
            f.write(chunk)
    return HttpResponse(file_path)

# Create your views here.

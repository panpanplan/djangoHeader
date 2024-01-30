import io
import json
import zipfile

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'GET':
        result = {
            'message': 'hello get'
        }
        return HttpResponse(result)
    elif request.method == 'POST':
        print(request.body)
        result = {
            'message': 'hello post'
        }
        return HttpResponse(result)


def download(request):
    if request.method == 'POST':
        z = {
            'message': 'hello',
            'errcode': '0'
        }
        stream = io.BytesIO()
        zFile = zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED, allowZip64=False)
        zFile.writestr("testfile.txt", json.dumps(z, ensure_ascii=False), zipfile.ZIP_DEFLATED)
        zFile.close()
        stream.seek(0)
        response = HttpResponse(stream.getvalue())
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Content-Disposition'
        response['Access-Control-Expose-Headers'] = 'Content-Disposition'   # **允许跨域后显示 Content-Disposition
        response['Content-Disposition'] = 'filename=data.zip'
        response['Content-Type'] = 'application/octet-stream'
        print(response)
        return response
    if request.method == 'GET':
        z = {
            'message': 'hello',
            'errcode': '0'
        }
        stream = io.BytesIO()
        zFile = zipfile.ZipFile(stream, 'w', zipfile.ZIP_DEFLATED, allowZip64=False)
        zFile.writestr("testfile.txt", json.dumps(z, ensure_ascii=False), zipfile.ZIP_DEFLATED)
        zFile.close()
        stream.seek(0)
        response = HttpResponse(stream.getvalue())
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Content-Disposition'
        response['Access-Control-Expose-Headers'] = 'Content-Disposition'
        response['Content-Disposition'] = 'attachment; filename=data.zip'
        response['Content-Type'] = 'application/octet-stream'
        return response

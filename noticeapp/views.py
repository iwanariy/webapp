# coding: utf-8
from django.shortcuts import render
from noticeapp.models import Notice


# GET /xxx/
def index(request):
    notices = Notice.objects.all()
    return render(request, 'index.html', {'notices': notices})

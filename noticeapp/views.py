# coding: utf-8
from django.shortcuts import render
from noticeapp.models import Notice

APP_NAME = 'noticeapp'


# GET /xxx/
def index(request):
    notices = Notice.objects.all()
    return render(request, '%s/index.html' % APP_NAME, {'notices': notices})

# coding: utf-8
from django.shortcuts import render


# GET /xxx/
def index(request):
    return render(request, 'index.html', {})

# encoding: utf-8
from django.shortcuts import render

APP_NAME = 'home'


def index(request):
    return render(request, '%s/index.html' % APP_NAME, {})

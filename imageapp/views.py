# encoding: utf-8
from django.shortcuts import render
from imageapp.models import Image

APP_NAME = 'imageapp'


def index(request):
    images = Image.objects.filter(is_published=True).order_by('published_at')

    return render(request, '%s/index.html' % APP_NAME, {'images': images})

# encoding: utf-8
from django.shortcuts import render
from imageapp.models import Image


def index(request):
    images = Image.objects.all()

    return render(request, 'image_list.html', {'images': images})

# encoding: utf-8
from django.shortcuts import render
from imageapp.models import Image


def index(request):
    images = Image.objects.filter(is_published=True).order_by('published_at')

    return render(request, 'image_list.html', {'images': images})

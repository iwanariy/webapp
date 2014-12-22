# coding: utf-8
from django.shortcuts import render
from formapp.forms import ContactForm


def contact_display(request):
    form = ContactForm()

    return render(request, 'contact_display.html', {'form': form})


def contact_complete(request):

    return render(request, 'contact_complete.html', {})

# coding: utf-8
from django.shortcuts import render
from formapp.forms import ContactForm


def contactform(request):
    form = ContactForm()

    return render(request, 'contact_display.html', {'form': form})

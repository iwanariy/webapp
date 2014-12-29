# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from formapp.forms import ContactForm


def contact_display(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('contact_complete/')
    else:
        form = ContactForm()

    return render(request, 'contact_display.html', {'form': form})


def contact_complete(request):

    return render(request, 'contact_complete.html', {})

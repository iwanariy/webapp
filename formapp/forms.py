# encoding: utf-8
from django.forms import ModelForm
from formapp.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('created_at',)

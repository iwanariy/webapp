# encoding: utf-8
from django.contrib import admin
from formapp.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail_address', 'title')

admin.site.register(Contact, ContactAdmin)

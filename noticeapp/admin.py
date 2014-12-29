# encoding: utf-8
from django.contrib import admin
from noticeapp.models import Notice


class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at',  'is_published')

admin.site.register(Notice, NoticeAdmin)

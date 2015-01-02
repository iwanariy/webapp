from django.conf.urls import patterns, url

urlpatterns = patterns(
    'noticeapp.views',
    url(r'^$', 'index'),
)

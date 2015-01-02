from django.conf.urls import patterns, url

urlpatterns = patterns(
    'imageapp.views',
    url(r'^$', 'index'),
)

from django.conf.urls import patterns, url

urlpatterns = patterns(
    'formapp.views',
    url(r'^$', 'contact_display'),
    url(r'^contact_complete/', 'contact_complete'),
)

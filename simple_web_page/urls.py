from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'simple_web_page.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', 'formapp.views.contact_display'),
    url(r'^contact/contact_complete/', 'formapp.views.contact_complete'),
    url(r'^notice/$', 'noticeapp.views.index'),
)

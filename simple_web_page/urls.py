from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'simple_web_page.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', 'formapp.views.contact_display'),
    url(r'^contact/contact_complete/', 'formapp.views.contact_complete'),
    url(r'^notice/$', 'noticeapp.views.index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

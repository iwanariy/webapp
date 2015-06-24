from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'webapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('formapp.urls')),
    url(r'^notice/', include('noticeapp.urls')),
    url(r'^image/', include('imageapp.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin

from odalc_billboard.app.views import IndexView, AJAXVoteView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^vote/$', AJAXVoteView.as_view(), name='vote'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

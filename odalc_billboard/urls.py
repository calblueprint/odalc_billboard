from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from odalc_billboard.app.views import IndexView, AJAXVoteView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^vote/$', AJAXVoteView.as_view(), name='vote'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

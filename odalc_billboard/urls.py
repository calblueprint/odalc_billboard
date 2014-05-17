from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from odalc_billboard.app.views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

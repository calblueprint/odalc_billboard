from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

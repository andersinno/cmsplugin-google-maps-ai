# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    # Serve media when in DEBUG mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

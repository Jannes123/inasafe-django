# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin


urlpatterns = patterns(
    '',

    # Enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # uncomment to enable defaut Django auth
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # include application urls
    url(r'', include('frontend.urls', namespace='front_end')),
    url(r'^user-map/', include('user_map.urls', namespace='user_map')),
    url(r'^realtime/', include('realtime.urls', namespace='realtime')),
    # url pattern for realtime reports
    url(r'', include('realtime.report_urls', namespace='realtime_report'))

)

# expose static files and uploded media if DEBUG is active
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True
            }),
        url(r'', include('django.contrib.staticfiles.urls'))
    )

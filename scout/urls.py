# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from campotec.auth import login as CampotecLogin, logout as CampotecLogout
from campotec.views import CampotecHomePageView, CampotecSpecialtiesInscriptionView, CampotecHomepagePreview, \
    CampotecInscriptionViews
from filebrowser.sites import site

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'scout.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # # filebrowser URLs
                       # url(r'^admin/filebrowser/', include(site.urls)),
                       # # grappelli URLs
                       # url(r'^grappelli/', include('grappelli.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^admin/filebrowser/', include(site.urls)),

                       url(r'^accounts/', include('registration.backends.default.urls')),
                       url(r'^campotec/', include('campotec.urls')),
                       url(r'^star_wars/', TemplateView.as_view(template_name='core/star_wars.html'), name='star_wars'),

                       # Institution
                       url(r'^institucional/',
                           include('institution.urls', namespace='institution', app_name='institution')),
                       url(r'^eventos/', include('events.urls', namespace='events', app_name='events')),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.SERVER_STATIC_FILES:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'core.views.error404'
handler400 = 'core.views.error500'
handler403 = 'core.views.error500'
handler500 = 'core.views.error500'
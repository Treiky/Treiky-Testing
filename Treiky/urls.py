from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # url(r'^$', 'IntentoTreiky.views.home', name='home'),
    # url(r'^IntentoTreiky/', include('IntentoTreiky.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # MediaURL
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
         'document_root': settings.MEDIA_ROOT,
         }),


    # Mi URL:
    url(r'^$', direct_to_template,
                   {'template': 'index.html'}, "home"),
    url(r'^accounts/profile/$', direct_to_template,
                   {'template': 'index.html'}, "home"),
    url(r'^home$', direct_to_template,
                   {'template': 'index.html'}, "home"),
    url(r'^write_req/$',
        'apps.requerimiento.views.write_req', name='write_req'),
    url(r'^view_req/$',
        'apps.requerimiento.views.view_req', name="view_req"),
    url(r'^write_project/$',
        'apps.requerimiento.views.write_project', name='write_project'),
    url(r'^new_user/$',
        'apps.requerimiento.views.new_user', name='new_user'),
    url(r'^resultado_usuario/$',
        'apps.requerimiento.views.resultado_alta_usuario',
        name='resultado_alta_usuario'),
    url(r'^resultado_proyecto/$',
        'apps.requerimiento.views.resultado_alta_proyecto',
        name='resultado_alta_proyecto'),
    url(r'^logout/$',
        'apps.requerimiento.views.logoutuser', name='logoutuser'),
    url(r'^search_project/$',
        'apps.requerimiento.views.searchProject', name='searchProject'),
    url(r'^update_project/$',
        'apps.requerimiento.views.update_project', name='updateproject'),
    url(r'^asigned_user/$',
        'apps.requerimiento.views.asig_user', name='asiguser'),
    url(r'^edit_user/$',
        'apps.requerimiento.views.edit_user', name='editUserForm'),
)

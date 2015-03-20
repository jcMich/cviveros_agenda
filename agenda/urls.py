from django.conf.urls import patterns, url

urlpatterns = patterns('agenda.views',
    url(r'^contacto/create/$', 'contacto_create', name='contacto_create'),
    url(r'^grupo/create/$', 'grupo_create', name='grupo_create'),
    url(r'^contactos/$', 'contactos_list', name='contactos_list'),
    url(r'^contacto/update/(?P<pk>.*)/$', 'contacto_update', name='contacto_update'),
    url(r'^contacto/delete/(?P<pk>.*)/$', 'contacto_delete', name='contacto_delete'),
    url(r'^contacto/search/$', 'contacto_search', name='contacto_search'),
    url(r'^grupo/update/(?P<pk>.*)/$', 'grupo_update', name='grupo_update'),
    url(r'^grupo/delete/(?P<pk>.*)/$', 'grupo_delete', name='grupo_delete'),
    url(r'^grupos/$', 'grupos_list', name='grupos_list'),
)

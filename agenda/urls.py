from django.conf.urls import patterns, url

urlpatterns = patterns('agenda.views',
    url(r'^contacto/create/$', 'contacto_create', name='contacto_create'),
    url(r'^grupo/create/$', 'grupo_create', name='grupo_create'),
    url(r'^color/create/$', 'color_create', name='color_create'),
    url(r'^contactos/$', 'contactos_list', name='contactos_list'),
    url(r'^contacto/update/(?P<pk>.*)/$', 'contacto_update', name='contacto_update'),
    url(r'^contacto/delete/(?P<pk>.*)/$', 'contacto_delete', name='contacto_delete'),
)

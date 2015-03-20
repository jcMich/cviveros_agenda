from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'christian.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', 'agenda.views.login_view', name='login'),
    url(r'^logout/', 'agenda.views.logout_view', name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^agenda/', include('agenda.urls')),
    )

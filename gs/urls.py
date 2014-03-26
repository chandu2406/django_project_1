from django.conf.urls import patterns, url

from gs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^comparison/$', views.comparison),
    url(r'^dashboard/$', views.dashboard),
    url(r'^allhomes/$', views.allhomes),
    url(r'^myhomes/$', views.myhomes),
    url(r'^(?P<review_id>\d+)/reviews/$', views.reviews, name='reviews'),
)
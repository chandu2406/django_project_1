from django.conf.urls import patterns, include, url
from django_project.api import UserResource

from django.contrib import admin
admin.autodiscover()

user_resource = UserResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(user_resource.urls)),

)

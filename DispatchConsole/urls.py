from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<iid>\d)/$', views.show, name='show'),
    url(r'^create/$', views.location_create),
    url(r'^update/$', views.update_location),

    #url(r'^posts/$', "<appname>.views.<funtion_name"),
]

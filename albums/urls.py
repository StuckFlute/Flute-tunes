from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.album_list, name='album_list'),
	url(r'^(?P<id>\d+)/$', views.album_detail, name='album_detail'),
    url(r'^(?P<id>\d+)/edit$', views.album_edit, name='album_edit'),
    url(r'^new/$', views.album_new, name='album_new'),
]
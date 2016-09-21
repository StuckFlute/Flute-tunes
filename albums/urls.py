from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.album_list, name='album_list'),
	url(r'^(?P<id>)\d+/$', views.album_detail, name='album_detail')
]
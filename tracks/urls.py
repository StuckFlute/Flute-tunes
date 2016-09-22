from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.track_list, name='track_list'),
	url(r'^artists/$', views.artist_list, name='artist_list'),
	url(r'^genres/$', views.genre_list, name='genre_list'),
	url(r'^(?P<id>\d+)/$', views.track_detail, name='track_detail')
]
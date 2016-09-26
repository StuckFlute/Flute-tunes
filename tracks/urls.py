from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.track_list, name='track_list'),
	url(r'^artists/$', views.artist_list, name='artist_list'),
	url(r'^genres/$', views.genre_list, name='genre_list'),
	url(r'^(?P<id>\d+)/$', views.track_detail, name='track_detail'),
    url(r'^(?P<id>\d+)/edit$', views.track_edit, name='track_edit'),
    url(r'^new/$', views.track_new, name='track_new'),

	url(r'^artists/(?P<id>\d+)/$', views.artist_detail, name='artist_detail'),
	url(r'^genres/(?P<id>\d+)/$', views.genre_detail, name='genre_detail'),

]
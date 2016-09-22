from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count

from .models import Artist, Genre, Track

def track_list(request):
	tracks = Track.objects.all()

	context = {
		"tracks": tracks,
	}
	return render(request, "tracks/track_list.html", context)

def track_detail(request, id):
	track = get_object_or_404(Track, pk=id)
	artists = track.artists.all()
	genres = track.genres.all()
	context = {
		"track": track,
		"artists":artists,
		"genres":genres
	}

	return render(request, "tracks/track_detail.html", context)

def artist_list(request):
	artists = Artist.objects.all()

	context = {
		"artists": artists,
	}
	return render(request, "tracks/artist_list.html", context)

def artist_detail(request, id):
	artist = get_object_or_404(Artist, pk=id)
	tracks = artist.track_set.all()

	context = {
		"tracks": tracks,
		"artist":artist,
	}

	return render(request, "tracks/artist_detail.html", context)

def genre_list(request):
	genres = Genre.objects.all()

	context = {
		"genres": genres,
	}
	return render(request, "tracks/genre_list.html", context)
def genre_detail(request, id):
	genre = get_object_or_404(Genre, pk=id)
	tracks = genre.track_set.all()
	context = {
		
		"genre":genre,
		"tracks": tracks,
	}

	return render(request, "tracks/genre_detail.html", context)

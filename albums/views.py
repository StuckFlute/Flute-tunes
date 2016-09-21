from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count

def album_list(request):
	albums = Album.objects.all()

	context = {
		"albums": albums,
	}
	return render(request, "albums/album_list.html", context)

def album_detail(request, id):
	album = get_object_or_404(Album, pk=id)

	context = {
		"album": album,
	}

	return render(request, "albums/album_detail.html", context)
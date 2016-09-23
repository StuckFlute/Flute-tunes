from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Count
from django.contrib import messages

from .models import Album
from .forms import AlbumForm

def album_list(request):
	albums = Album.objects.all()

	context = {
		"albums": albums,
	}
	return render(request, "albums/album_list.html", context)

def album_detail(request, id):
	album = get_object_or_404(Album, pk=id)
	tracks = album.track_set.all()

	context = {
		"album": album,
		"tracks": tracks,
	}

	return render(request, "albums/album_detail.html", context)

def album_new(request):

	if request.method == "POST":
		form = AlbumForm(request.POST)
		if form.is_valid():
			album = form.save()
			messages.success(request,"Album created!")
			return redirect("albums:album_detail",id=album.pk)
	else:
		form = AlbumForm()

	context = {
		"form":form,
	}
	return render(request,"albums/album_edit.html",context)

def album_edit(request,id):
	album = get_object_or_404(Album,pk=id)

	if request.method == "POST":
		form = AlbumForm(request.POST, instance=album)
		if form.is_valid():
			album = form.save()
			messages.success(request,"Album updated!")
			return redirect("albums:album_detail",id=album.pk)
	else:
		form = AlbumForm(instance=album)

	context = {
		"form":form,
		"album":album,
	}
	return render(request,"albums/album_edit.html",context)
from django.contrib import admin
from .models import Album
from tracks.models import Track

track=Track()
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('title',)

    list_display = ['title','track_titles']

    def track_titles(self,obj):
        names = [t.title for t in obj.track_set.all()]
        return ", ".join(names)

    track_titles.short_description = 'Track Titles'

admin.site.register(Album,AlbumAdmin)
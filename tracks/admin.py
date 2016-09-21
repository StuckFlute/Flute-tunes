from django.contrib import admin
from .models import Track, Artist, Genre

class TrackAdmin(admin.ModelAdmin):
    list_display = ['title','album','track_number','artist_names','genre_names']

    def artist_names(self,obj):
        names = [artist.name for artist in obj.artists.all()]
        return ", ".join(names)

    artist_names.short_description = 'Artists'

    def genre_names(self,obj):
        names = [genre.name for genre in obj.genres.all()]
        return ", ".join(names)
        
    genre_names.short_description = 'Genres'

class ArtistInLine(admin.StackedInline):
    model = Track.artists.through
    extra = 0

class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [ArtistInLine,]

class GenreInLine(admin.StackedInline):
    model = Track.genres.through
    extra = 0

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [GenreInLine,]

admin.site.register(Track,TrackAdmin)
admin.site.register(Artist,ArtistAdmin)
admin.site.register(Genre,GenreAdmin)


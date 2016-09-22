from django.db import models
from django.core.urlresolvers import reverse


class Track(models.Model):

    title =models.CharField(max_length =100,blank=True)
    album = models.ForeignKey('albums.Album',null=True,blank=True)
    artists = models.ManyToManyField('Artist',blank=True)
    genres = models.ManyToManyField('Genre',blank=True)    
    track_number = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tracks:track_detail', args=[self.pk])

class Artist(models.Model):

    name =models.CharField(max_length =100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('tracks:artist_detail', args=[self.pk])


class Genre(models.Model):

    name =models.CharField(max_length =100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('tracks:genre_detail', args=[self.pk])



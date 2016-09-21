from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField (blank=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


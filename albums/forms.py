from django import forms
from .models import Album
from core.forms import BootstrapFormMixin

class AlbumForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title','description',)

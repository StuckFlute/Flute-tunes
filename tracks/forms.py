from django import forms
from .models import Track
from core.forms import BootstrapFormMixin

class TrackForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Track
        fields = ('title','album','artists','genres','track_number',)

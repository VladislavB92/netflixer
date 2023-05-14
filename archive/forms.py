from django.forms import ModelForm
from archive.models import Movie


class MovieForm(ModelForm):
    """A modelform class for the Movie objects."""

    class Meta:
        model = Movie
        fields = ['title', 'director', 'year']

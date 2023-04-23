from sqlite3 import DatabaseError
from archive.models import Movie
from django.contrib import messages


def delete_movie_object(object_id, request):
    """Deletes the movie object from the list according to the id."""
    try:
        movie = Movie.objects.get(id=object_id)
        movie.delete()
        messages.success(request, 'The movie has been deleted.')
    except DatabaseError:
        messages.error(request, 'Something went wrong. Contact devs.')

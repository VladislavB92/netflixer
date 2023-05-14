from archive.forms import MovieForm
from archive.models import Movie
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from archive.utils import delete_movie_object
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)


class AllMovies(LoginRequiredMixin, ListView):
    """
    A view that get all movie objects from the database,
    puts it in the context and outputs to the HTML template.
    No forms are used here.
    As a context key in the HTML, the 'object_list' is used.
    """
    template_name = 'all_movies.html'
    model = Movie


class SingleMovie(DetailView):
    template_name = 'movie.html'
    model = Movie


class AddMovieView(LoginRequiredMixin, CreateView):
    """
    Renders(opens) a new add movie HTML template,
    provides a form with inputs and tries to save the movie to the database
    base on the values that come from the request.POST (dictionary).
    If the request.POST is empty, then the HTML is rendered(refreshed) successfully.
    After either successful or unsuccessful new movie creation, the user is redirected to the
    all movies page.
    """

    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = '/'


class UpdateMovieView(LoginRequiredMixin, UpdateView):

    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_url = '/'


def delete_movie(request, movie_id):
    """It is a GET method (because we pass movie_id as a URL parameter to get
    the movie we want to delete from the database.
    A delete_movie_object() function is used here to locate and try to delete the movie
    we queried in the URL parameter.
    In all cases we are being redirected back to the all movies list.
    """
    delete_movie_object(movie_id, request)
    return redirect('all-movies')

from archive.forms import MovieForm
from archive.models import Movie
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    View,
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


class DeleteMovieView(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        movie = Movie.objects.get(id=kwargs.get('pk'))
        movie.delete()
        return redirect('all-movies')

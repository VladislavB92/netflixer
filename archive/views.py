from django.contrib import messages
from django.http import Http404
from archive.models import Movie
from django.shortcuts import render, redirect

from archive.utils import delete_movie_object


def get_all_movies(request):
    """
    A view that get all movie objects from the database,
    puts it in the context and outputs to the HTML template.
    No forms are used here.
    """
    all_movies = Movie.objects.all()

    context = {
        'all_movies_list': all_movies,
    }
    return render(request, 'all_movies.html', context)


def add_movie(request):
    """
    Renders(opens) a new add movie HTML template,
    provides a form with inputs and tries to save the movie to the database
    base on the values that come from the request.POST (dictionary).
    If the request.POST is empty, then the HTML is rendered(refreshed) successfully.
    After either successful or unsuccessful new movie creation, the user is redirected to the
    all movies page.
    """
    if request.POST:
        title = request.POST.get('title')
        director = request.POST.get('director')
        year = request.POST.get('year')
        try:
            new_movie = Movie.objects.create(
                title=title,
                director=director,
                year=year,
            )
            new_movie.save()
            messages.success(request, 'The movie has been saved.')
        except ValueError:
            messages.error(request, 'Something went wrong. Contact devs.')
        return redirect('all-movies')
    context = {}
    return render(request, 'add_movie.html', context)


def get_movie(request, movie_id):
    """
    A view got two logics.
    First: a POST request, that sends us the ID of the movie we want to delete,
    after we press the Delete button in the HTML template.
    Then the movie is deleted, and we are redirected back to the all movies page.
    Same goes if movie deletion was not successful.
    Second: we try to get the movie with the movie_id that we pass to the
    URL as parameter (GET method) and show movie details on the page.
    """
    if request.POST:
        movie_to_delete = request.POST.get('movie_to_delete')
        delete_movie_object(movie_to_delete, request)
        return redirect('all-movies')

    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        raise Http404('Movie does not exists')
    context = {}
    if movie:
        context.update({'movie': movie})
    return render(request, 'movie.html', context)


def delete_movie(request, movie_id):
    """It is a GET method (because we pass movie_id as a URL parameter to get
    the movie we want to delete from the database.
    A delete_movie_object() function is used here to locate and try to delete the movie
    we queried in the URL parameter.
    In all cases we are being redirected back to the all movies list.
    """
    delete_movie_object(movie_id, request)
    return redirect('all-movies')

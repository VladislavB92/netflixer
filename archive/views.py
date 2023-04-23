from django.contrib import messages
from django.http import Http404
from archive.models import Movie
from django.shortcuts import render, redirect


def get_all_movies(request):
    all_movies = Movie.objects.all()

    context = {
        'all_movies_list': all_movies,
    }
    return render(request, 'all_movies.html', context)


def add_movie(request):
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
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        raise Http404('Movie does not exists')
    context = {}
    if movie:
        context.update({'movie': movie})
    return render(request, 'movie.html', context)


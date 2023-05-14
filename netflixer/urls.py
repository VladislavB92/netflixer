from django.contrib import admin
from django.urls import path, include

from archive.views import (
    AddMovieView,
    delete_movie,
    AllMovies,
    SingleMovie,
    UpdateMovieView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', AllMovies.as_view(), name='all-movies'),
    path('add-movie/', AddMovieView.as_view(), name='add-movie'),
    path('edit-movie/<int:pk>', UpdateMovieView.as_view(), name='edit-movie'),
    path('movie/<int:pk>/', SingleMovie.as_view(), name='get-movie'),
    path('delete/<movie_id>', delete_movie, name='delete-movie'),
]

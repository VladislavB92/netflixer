from django.contrib import admin
from django.urls import path, include

from archive.views import (
    AddMovieView,
    DeleteMovieView,
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
    path('delete/<int:pk>/', DeleteMovieView.as_view(), name='delete-movie'),
]

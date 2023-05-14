"""
URL configuration for netflixer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from archive.views import AddMovieView, delete_movie, AllMovies, SingleMovie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', AllMovies.as_view(), name='all-movies'),
    path('add-movie/', AddMovieView.as_view(), name='add-movie'),
    path('movie/<int:pk>/', SingleMovie.as_view(), name='get-movie'),
    path('delete/<movie_id>', delete_movie, name='delete-movie'),
]

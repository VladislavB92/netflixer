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
from django.urls import path

from archive.views import get_all_movies, add_movie, get_movie, delete_movie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_all_movies, name='all-movies'),
    path('add-movie/', add_movie, name='add-movie'),
    path('movie/<movie_id>/', get_movie, name='get-movie'),
    path('delete/<movie_id>', delete_movie, name='delete-movie'),
]

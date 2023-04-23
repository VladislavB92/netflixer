from django.contrib import admin
from archive.models import Movie


# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    pass


admin.site.register(Movie, MovieAdmin)

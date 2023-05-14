from django.db import models


class Movie(models.Model):
    title = models.CharField(null=False, blank=False, max_length=128)
    director = models.CharField(null=False, blank=True, max_length=128)
    year = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.title} - {self.year}'

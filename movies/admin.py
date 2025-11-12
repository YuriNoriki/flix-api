from django.contrib import admin
from movies.models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'genre', 'realese_date',
        'actors', 'resume',
    )

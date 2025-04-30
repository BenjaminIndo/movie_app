from django.contrib import admin
from movie_app.models import Movie, Review

admin.site.register([Movie])
admin.site.register([Review])

# Register your models here.

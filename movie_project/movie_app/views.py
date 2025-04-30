from django.shortcuts import render, redirect

from movie_app.models import Movie, Review

def movies(request):
    my_movies = Movie.objects.all()
    if request.method =="GET":
        return render(request, "movie_app/index.html",{"movies":my_movies})
    if request.method =="POST":
        title = request.POST["title"]
        description = request.POST["description"]
        releaseDate = request.POST["release-date"]
        poster = request.FILES.get("poster")
        newMovie = Movie(title=title, description=description, release_date = releaseDate, poster=poster)
        newMovie.save()
        return redirect("/movies")
# Create your views here.

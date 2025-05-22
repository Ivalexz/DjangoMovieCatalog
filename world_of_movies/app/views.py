from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view

from world_of_movies.app.forms import AddMovieForm, UpdateMovieForm, SearchMovieForm
from world_of_movies.app.models import Movie
from world_of_movies.app.serializers import MovieSerializer


def get_all_movies(request): # функція і фільтрує і виводить усі фільми
    form=SearchMovieForm(request.GET or None)
    filtered_movies=Movie.objects.all()

    if form.is_valid():
        min_year=form.cleaned_data.get("min_year") or 1896
        max_year=form.cleaned_data.get("max_year") or 2025
        min_rating = form.cleaned_data.get("min_rating") or 0
        max_rating = form.cleaned_data.get("max_rating") or 5
        title = form.cleaned_data.get("title")
        director = form.cleaned_data.get("director")
        genre = form.cleaned_data.get("genre")

        filtered_movies = filtered_movies.filter(
            year__gte=min_year,
            year__lte=max_year,
            rating__gte=min_rating,
            rating__lte=max_rating
        )
        if title:
            filtered_movies = filtered_movies.filter(title__icontains=title)
        if director:
            filtered_movies = filtered_movies.filter(director__icontains=director)
        if genre:
            filtered_movies = filtered_movies.filter(genre__icontains=genre)

    context={
        "movies" : filtered_movies,
        "form" : form,
    }
    return render(request, 'app/movie_list.html', context)

def get_movie_by_id(request, movie_id):
    movie=get_object_or_404(Movie, id=movie_id)
    context={
        "movie_id": movie_id,
        "movie": movie
    }
    return render(request, 'app/movie_details.html', context)

def add_movie(request):
    form = AddMovieForm(request.POST or None)
    if form.is_valid():
        Movie.objects.create(
            cover=form.cleaned_data.get("cover"),
            title=form.cleaned_data.get("title"),
            director=form.cleaned_data.get("director"),
            year=form.cleaned_data.get("year"),
            genre=form.cleaned_data.get("genre"),
            rating=form.cleaned_data.get("rating")
        )
        return redirect("app:get_all_movies")

    context={
        "form": form
    }
    return render(request, "app/add_movie.html", context)

def delete_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    movie.delete()
    return redirect('app:get_all_movies')

def update_movie(request, movie_id):
    form=UpdateMovieForm(request.POST or None)
    if form.is_valid():
        movie = Movie.objects.get(id=movie_id)
        if form.cleaned_data.get("cover"):
            movie.cover=form.cleaned_data["cover"]
        if form.cleaned_data.get("title"):
            movie.title = form.cleaned_data["title"]
        if form.cleaned_data.get("director"):
            movie.director = form.cleaned_data["director"]
        if form.cleaned_data.get("year"):
            movie.year = form.cleaned_data["year"]
        if form.cleaned_data.get("genre"):
            movie.genre = form.cleaned_data["genre"]
        if form.cleaned_data.get("rating"):
            movie.rating=form.cleaned_data["rating"]
        movie.save()
        return redirect('app:get_all_movies')

    context={
        "form": form
    }
    return render(request, 'app/update_movie.html', context)


@api_view(['GET'])
def movie_list_api(request):
    all_movies=Movie.objects.all()
    serializer=MovieSerializer(all_movies, many=True) #перетворює у JSON
    return JsonResponse(serializer.data, safe=False) #гарно відформатований JSON; save=False тому що відправляємо list, а не dict
from django.urls import path
from . import views

app_name = "app"

urlpatterns=[
    path('', views.get_all_movies, name="get_all_movies"), #http://127.0.0.1:8000
    path('movie/add/', views.add_movie, name='add_movie'),
    path('movie/update/<int:movie_id>/', views.update_movie, name='update_movie'),
    path('movie/delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('movie/details/<int:movie_id>/', views.get_movie_by_id, name='movie_details'),
    path("api/movies/", views.movie_list_api, name="movie_list_api")
]

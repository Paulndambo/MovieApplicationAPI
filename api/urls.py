from django.urls import path
from . import views


urlpatterns = [ 
    path("movies/", views.MoviesListCreateAPIView.as_view(), name="movies"),
    path("movies/<int:movie_id>/", views.MovieDetailByMovieID.as_view(), name="movie-details"),
    path("movies/<str:imdb_id>/", views.MovieDetailByMovieImdbID.as_view(), name="movie-more-details"),
    path("comments/", views.CommentListCreateAPIView.as_view(), name="comments"),
    path("movies/<int:movie_id>/comments/", views.MovieCommentListAPIView.as_view(), name="movie-comments"),
]
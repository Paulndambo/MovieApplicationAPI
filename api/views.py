from django.shortcuts import render, get_object_or_404
from .serializers import MovieSerializer, CommentSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Movie, Comment
from rest_framework import generics, status
from rest_framework.response import Response
import requests

# Create your views here.

#Creating and listing movies
class MoviesListCreateAPIView(generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, movie_id=None):
        movies =  Movie.objects.all().order_by("-created_at")
        serializer = self.serializer_class(instance=movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        title = data['title']
        serializer = self.serializer_class(data=data)
        if title:
            try:
                #request data from imdb and filter by title passed
                imdb_endpoint = f"http://www.omdbapi.com/?t={title}&apikey=5ded9f17"
                movie = requests.get(imdb_endpoint).json()
                if movie:
                    if serializer.is_valid():
                        serializer.save(
                            title = movie['Title'],
                            rated = movie['Rated'],
                            released = movie['Released'],
                            runtime = movie['Runtime'],
                            genre = movie['Genre'],
                            director = movie['Director'],
                            writer = movie['Writer'],
                            actors = movie['Actors'],
                            plot = movie['Plot'],
                            language = movie['Language'],
                            country = movie['Country'],
                            poster = movie['Poster'],
                            ratings = movie['Ratings'],
                            metascore = movie['Metascore'],
                            imdb_rating = movie['imdbRating'],
                            imdb_votes = movie['imdbVotes'],
                            imdb_id = movie['imdbID'],
                            type = movie['Type'],
                            total_seasons = movie.get('totalSeasons', 0),
                            response = movie['Response'],
                            year = movie['Year'],
                        )
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response({"message": "Movie With This Title Does Not Exist"})
            except Exception as e:
                raise e
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#get movie details by movie id
class MovieDetailByMovieID(generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = self.serializer_class(instance=movie)
        return Response(serializer.data, status=status.HTTP_200_OK)


#get movie details by imdb id
class MovieDetailByMovieImdbID(generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get(self, request, imdb_id):
        movie = Movie.objects.filter(imdb_id=imdb_id)
        serializer = self.serializer_class(instance=movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#Create and list comments without filters
class CommentListCreateAPIView(generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request):
        comments = Comment.objects.all().order_by("-created_at")
        serializer = self.serializer_class(instance=comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Listing comments filtered by movie id
class MovieCommentListAPIView(generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, movie_id):
        movie = Movie.objects.get(pk=movie_id)
        comments = Comment.objects.filter(movie=movie)
        serializer = self.serializer_class(instance=comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

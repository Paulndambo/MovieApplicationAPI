import pytest 
import requests
import json
movies_url = "http://127.0.0.1:8000/api"



def test_get_movies():
    url = movies_url +"/movies/"
    resp = requests.get(url)
    assert resp.status_code == 200


def test_post_movies():
    url = movies_url + "/movies/"
    title = "Shooter"
    imdb_url = f"http://www.omdbapi.com/?t={title}&apikey=5ded9f17"
    movie = requests.get(imdb_url).json()
    data = {
        "title": movie['Title'],
        "rated": movie['Rated'],
        "released":  movie['Released'],
        "runtime": movie['Runtime'],
        "genre": movie['Genre'],
        "director": movie['Director'],
        "writer": movie['Writer'],
        "actors": movie['Actors'],
        "plot": movie['Plot'],
        "language": movie['Language'],
        "country": movie['Country'],
        "poster": movie['Poster'],
        "ratings": movie['Ratings'],
        "metascore": movie['Metascore'],
        "imdb_rating": movie['imdbRating'],
        "imdb_votes": movie['imdbVotes'],
        "imdb_id": movie['imdbID'],
        "type": movie['Type'],
        "total_seasons": movie.get('totalSeasons', 0),
        "response": movie['Response'],
        "year": movie['Year'],
    }
    resp = requests.post(url, data)
    assert resp.status_code == 200

def test_get_movie_details():
    movie_id = 11
    url = f"{movies_url}/movies/{movie_id}"
    resp = requests.get(url)
    assert resp.status_code == 200
                              
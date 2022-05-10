import requests

apiKey = "5ded9f17"
title = "Shooter"
endpoint = f"http://www.omdbapi.com/?t={title}&apikey=5ded9f17"
movie = requests.get(endpoint).json()
title = movie['Title']
rated = movie['Rated']
released = movie['Released']
runtime = movie['Runtime']
genre = movie['Genre']
director = movie['Director']
writer = movie['Writer']
actors = movie['Actors']
plot = movie['Plot']
language = movie['Language']
country = movie['Country']
poster = movie['Poster']
ratings = movie['Ratings']
metascore = movie['Metascore']
imdb_rating = movie['imdbRating']
imdb_votes = movie['imdbVotes']
imdb_id = movie['imdbID']
type = movie['Type']
total_seasons = movie.get('totalSeasons')
response = movie['Response']
print(total_seasons)
from collections import namedtuple

Movie = namedtuple("Movie", ["title", "year", "director", "genre"])

print(Movie)

movie = Movie("Terminator", "1992", "James Cameron", "action")

print(movie.title)
print(movie.year)
print(movie.director)
print(movie.genre)

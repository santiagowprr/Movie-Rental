from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return f"<User {self.name}>"

    def add_movie(self, name, genre):
        new_movie = Movie(name, genre, False)
        self.movies.append(new_movie)

    def delete_movie(self, name):
        # movie_to_delete = Movie(name)
        # self.movies.pop(movie_to_delete)
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        return list(filter(lambda x: x.watched, self.movies))
  
    def json(self):
        return {
            'name': self.name,
            'movies': [
                movie.json() for movie in self.movies
            ]
        }

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user


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
         
    def save_to_file(self):
        with open(f"{self.name}.txt", 'w') as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write(f"{movie.name},{movie.genre},{str(movie.watched)}\n")

    
    def load_from_file(self,filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            username = content[0]
            movies = []
            for line in content[1:]:
                movie_data = line.split(",")  #[name', 'genre', 'watched']
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))

            user = User(username)
            user.movies = movies
            return user
class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return f"<User {self.name}>"

    def watched_movies(self):
        watched_movies_list = []
        
        for movie in self.movies:
            if movie.watched:
                watched_movies_list.append(movie)
        return watched_movies_list


from user import User
import json
import os

def menu():
    name = input("What's your name?")
    filename = f"{name}.txt"
    if file_exists(filename):
        with open(filename, 'r') as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)
    
    print("Select what do you want to do!")
    print("1. Add a movie")
    print("2. See list of movies")
    print("3. Set a movie as watched")
    print("4. Delete a movie by name")
    print("5. See list of watched movies")
    print("6. Save")
    print("0. Quit")
    user_input = int(input(""))

    while user_input != 0:
        if user_input == 1:
            new_movie_name = input("Insert the name of the new movie:\n")
            new_movie_genre = input("Insert the genre of the new movie:\n")
            user.add_movie(new_movie_name, new_movie_genre)
        
        elif user_input == 2:
            for movie in user.movies:
                print(f"Name: {movie.name}, Genre: {movie.genre}, Watched: {movie.watched}")
        
        elif user_input == 3:
            movie_to_set = input("What movie do you want to set as watched?")
            user.set_watched(movie_to_set)

        elif user_input == 4:
            movie_to_delete = input("What movie do you want to delete?")
            user.delete_movie(movie_to_delete)

        elif user_input == 5:
            for movie in user.watched_movies():
                print(f"Name: {movie.name}, Genre: {movie.genre}, Watched: {movie.watched}")

        if user_input == 6:
            with open (filename, 'w') as f:
                json.dump(user.json(), f)

        print("Select what do you want to do!")
        print("1. Add a movie")
        print("2. See list of movies")
        print("3. Set a movie as watched")
        print("4. Delete a movie by name")
        print("5. See list of watched movies")
        print("6. Save")
        print("0. Quit")        
        user_input = int(input(""))


def file_exists(filename):
    return os.path.isfile(filename)


menu()
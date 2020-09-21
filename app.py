from user import User

user = User('Jose')

user = user.load_from_file('Jose.txt')

print(user.movies)
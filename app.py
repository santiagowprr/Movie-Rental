from user import User

user = User.load_from_file('Jose.txt')

print(user.name)
print(user.movies)
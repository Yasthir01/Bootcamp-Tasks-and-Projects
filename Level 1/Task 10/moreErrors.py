"""A program with two compilation errors, a runtime error and a logical error"""


# I will be using a program that asks a user if they want to watch a movie

# create a list of movies that are available to watch
available_movies = ['The Matrix', 'Pirates of the Caribbean', 'The Dark Knight', 'Inception',
					'Intersteller', 'Mr Nobody', 'Memento', 'Fight Club', 'Donnie Darko']

# ask the user if they want to watch a movie
user_input = input("Would you like to watch a movie? (Type 'Y' or 'N') : ").lower()

# if the user says they want to watch a movie, then print out the list of movies
if user_input == 'y':
	for available_movie in available_movies:
		print(available_movies)  # Logical Error. It is supposed to be available_movie, not available_movies
# if they dont want to watch a movie right now
elif user_input == n:  # Runtime error. It is a name error. Its meant to be a string 'n', not n
print "Okay, see you next time :)"   # Compilation Error. Print Statement is meant to be indented
									 # Compilation Error. Print statement is missing parentheses

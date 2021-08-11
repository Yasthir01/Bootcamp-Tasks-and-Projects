import spacy

nlp = spacy.load('en_core_web_md')

# open the movies.txt file
file = open('movies.txt')
content = file.readlines()

# save the description to a variable
hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the\
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a\
planet where the Hulk can live in peace. Unfortunately, Hulk land on the\
planet Sakaar where he is sold into slavery and trained as a gladiator."

movie_comparison = nlp(hulk_description)


def movie_recommendation(description):
	"""Determines which movie a user should watch next"""
	movie_comparison = nlp(hulk_description)

	# create an empty list that will store the values
	similar_movies = []

	# iterate through each line in the file
	for line in content:
		# we need to remove the word movie
		movie, description = line.split(':')  # split at the colon in each line
		movie_now = nlp(description)  # we just needed the description
		# use similarity to get values
		similar = movie_now.similarity(movie_comparison)
		# append each value to the list we created earlier
		similar_movies.append(similar)

	# we need to find the highest value in the list
	highest_value = max(similar_movies)
	# use the index method to find position of highest value
	movie_index = similar_movies.index(highest_value)

	return content[movie_index]  # returns the actual movie at that index

print(movie_recommendation(hulk_description))






"""Using Spacy on garden path sentences"""

import spacy

 # load the english language model
nlp = spacy.load("en_core_web_sm") 

# create garden path sentences
flower = "The florist sent the flowers was pleased"
cotton = "The cotton clothing is made of grows in Mississippi"
drink = "The sour drink from the ocean"
students = "Have the students who failed the exam take the supplementary"
girl = "The girl told the story cried"

# store sentences in a list
garden_path_sentences = [flower, cotton, drink, students, girl]

# loop through the list
for sentence in garden_path_sentences:
	for i in nlp(sentence).ents:
		print(i, i.label_, i.label)
"""Creating functions"""


def days_of_week():
	"""Prints out all the days of the week"""
	print('Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday')


def replace_hello(sentence):
	"""Replaces every second word with 'Hello' """
	# split the sentence where there is a blank space
	my_list = sentence.split(' ')
	# get every second element
	second_element = my_list[::2]
	# create an empty list that will be used for the final sentence
	final = []
	# iterate through the second_element list and append a word and then Hello
	for word in second_element:
		final.append(word)
		final.append("Hello") 
	# take the elements in the list and join it into a single string
	final_sentence = " ".join(final)
	print(final_sentence)
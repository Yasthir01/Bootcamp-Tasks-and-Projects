"""A program that displays the names of incorrect entries"""


incorrect_list = []  # list to store the incorrect names entered
desired_name = 'John'  # we want the user to input John

while True:
	name = input("Enter your name: ")
	if name == desired_name:
		break
	incorrect_list.append(name)  # append the incorrect name through every iteration

print(f"Incorrect names: {incorrect_list}")

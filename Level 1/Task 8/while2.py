"""Program that keeps asking a user to enter their name until they enter the correct one"""


name = "Yasthir"  # I will be using my own name
counter = 1  # this will keep track of the number of tries 

# get user input about their name
name_guess = input("Please enter in your name  (type 'q' to quit) : ")

# keep on asking the user their name until they get it right
while name_guess != name:
	name_guess = input("Please enter in your name  (type 'q' to quit) : ")
	if name_guess == 'q':
		break
	counter += 1
	
# we dont want the counter to be displayed if the user quits the program
if name_guess != 'q':
	print(f"It took you {counter} tries")






"""A program about password strength"""


# declaring boolean variables
have_length = False  # length of the password
up_case = False  # needs to contain uppercase letters
low_case = False  # needs to contain lowercase letters
have_num = False  # needs to contain numbers

requirements = 0  # this will be a counter variable that I will increment everytime requirement is met

""" A series of Yes or No questions """

# check the length of the password
length_question = input("Is your password at least 6 characters long? (Yes or No): ")
if length_question == 'Yes':
	have_length = True
	requirements += 1
elif length_question == 'No':
	print('Your password needs to be at least 6 characters long!')

# check whether the password contains uppercase letters
upper_case_question = input("Does your password contain uppercase letters? (Yes or No): ")
if upper_case_question == 'Yes':
	up_case = True
	requirements += 1
elif upper_case_question == 'No':
	print("Your password needs to contain uppercase letters!")

# check whether the password contains lowercase letters
lower_case_question = input("Does your password contain lowercase letters? (Yes or No): ")
if lower_case_question == 'Yes':
	low_case = True
	requirements += 1
elif lower_case_question == 'No':
	print("Your password needs to contain lowercase letters!")

# check whether the password contains numbers
have_nums_question = input("Does your password contain numbers? (Yes or No): ")
if have_nums_question == 'Yes':
	have_num = True
	requirements += 1
elif have_nums_question == 'No':
	print("Your password needs to contain numbers!")

# check the length of the password requirements
# if it contains more than 3 then it is suitable
if requirements >= 3:
	print("You have chosen a suitable password!")
else:
	print("You password is not secure!")
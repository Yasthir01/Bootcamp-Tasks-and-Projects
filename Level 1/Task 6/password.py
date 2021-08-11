"""A program about password strength"""


# declaring boolean variables
have_length = False  # length of the password
up_case = False  # needs to contain uppercase letters
low_case = False  # needs to contain lowercase letters
have_num = False  # needs to contain numbers



requirements_list = []  # I will store the True values inside this list

""" A series of Yes or No questions """

length_question = input("Is your password at least 6 characters long? (Yes or No): ")
if length_question == 'Yes':
	have_length = True
	requirements_list.append(have_length)
elif length_question == 'No':
	print('Your password needs to be at least 6 characters long!')


upper_case_question = input("Does your password contain uppercase letters? (Yes or No): ")
if upper_case_question == 'Yes':
	up_case = True
	requirements_list.append(up_case)
elif upper_case_question == 'No':
	print("Your password needs to contain uppercase letters!")


lower_case_question = input("Does your password contain lowercase letters? (Yes or No): ")
if lower_case_question == 'Yes':
	low_case = True
	requirements_list.append(low_case)
elif lower_case_question == 'No':
	print("Your password needs to contain lowercase letters!")


have_nums_question = input("Does your password contain numbers? (Yes or No): ")
if have_nums_question == 'Yes':
	have_num = True
	requirements_list.append(have_num)
elif have_nums_question == 'No':
	print("Your password needs to contain numbers!")



# check the length of the password requirements list
# if it contains more than 3 then it is suitable
if len(requirements_list) >= 3:
	print("You have chosen a suitable password!")
else:
	print("You password is not secure!")



"""N.B. I know I probably shouldn't have used lists in this task as it hasn't been discussed yet, 
	but I didnt know how else to efficiently do it"""
"""Program to check whether a number entered by a user is a prime number"""


# get integer from user
user_num = int(input("Enter in a number: "))

# first check if the number is greater than 1
if user_num > 1:
	# check the range of 2 to the number itself
	for i in range(2, user_num):
		if user_num % i == 0:  # if there are no remainders then it is not a prime number
			print(f"{user_num} is not a prime number")
			break
	else:
		print(f"{user_num} is a prime number")

# if the number is not greater than 1
else:
	print(f"{user_num} is not a prime number")


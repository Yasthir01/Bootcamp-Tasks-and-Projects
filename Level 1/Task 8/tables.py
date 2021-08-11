"""A program that displays the multiplication table for an entered number"""


# ask the user to enter in number for multiplication table
user_num = int(input("Please enter in a number: "))

# for loop going up to 12
for i in range(1, 13):
	print(f"{user_num} x {i} = {user_num * i}")

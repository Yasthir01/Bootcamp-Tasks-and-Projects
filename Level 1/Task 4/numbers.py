"""Getting numbers from a user and then performing arithmetic operations"""



# get 3 numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


# get the sum of the numbers
sum_of_nums = num1 + num2 + num3
print(f"The sum of the numbers are: {sum_of_nums}")

# first number minus the second number
print(f"First number minus second number: {num1 - num2}")

# third number multiplied by the first number
print(f"Third number multiplied by the first number: {num3 * num1}")

# sum of all 3 numbers divided by third number
print(f"The sum of all 3 numbers divided by the third number: {sum_of_nums / num3}")
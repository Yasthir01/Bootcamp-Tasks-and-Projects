"""Program that evaluates a person's age"""


# take in user's age
age = int(input("Please enter in your age: "))

# evaluate the input 
if age >= 18:
	print("You are old enough!")
elif age >= 16:
	print("Almost there")
else:
	print("You're just too young!")
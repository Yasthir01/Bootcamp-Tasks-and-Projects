"""Using input function to get information from user"""


name = input("Enter your name: ")
age = int(input("Enter your age: "))
house_num = int(input("Enter your house number: "))
street_name = input("Enter your street name: ")

# print out a single sentence containing all details of the user
print(f"This is {name} who is {age} years old and lives at house number {house_num} on {street_name}.")